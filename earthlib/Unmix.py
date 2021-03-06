"""Routines for performing spectral unmixing on earth engine images."""

import ee as _ee
from tqdm import tqdm as _tqdm

from .utils import selectSpectra as _selectSpectra


# this function must be run before any of the specific unmixing routines are set
def Initialize(sensor, n=30, bands=None):
    """Initializes sensor-specific global variables.

    Args:
        sensor: the name of the sensor (from earthlib.listSensors()).
        n: the number of iterations for unmixing.
        bands: a list of bands to select (from earthlib.getBands(sensor)).

    Returns:
        None: creates a series of global endmember variables.
    """

    # get them as a python array
    pv_list = _selectSpectra("vegetation", sensor, n, bands)
    npv_list = _selectSpectra("npv", sensor, n, bands)
    soil_list = _selectSpectra("bare", sensor, n, bands)
    burn_list = _selectSpectra("burn", sensor, n, bands)
    urban_list = _selectSpectra("urban", sensor, n, bands)

    # create a series of global variables for later
    global pv
    global npv
    global soil
    global burn
    global urban

    # then convert them to ee lists
    pv = [_ee.List(pv_spectra.tolist()) for pv_spectra in pv_list]
    npv = [_ee.List(npv_spectra.tolist()) for npv_spectra in npv_list]
    soil = [_ee.List(soil_spectra.tolist()) for soil_spectra in soil_list]
    burn = [_ee.List(burn_spectra.tolist()) for burn_spectra in burn_list]
    urban = [_ee.List(urban_spectra.tolist()) for urban_spectra in urban_list]


def fractionalCover(
    img,
    endmembers,
    endmember_names,
    shade_normalize=False,
):
    """Computes the percent cover of each endmember spectra.

    Args:
        img: the ee.Image to unmix.
        endmembers: lists of ee.List objects, each element corresponding to a sub.
        endmember_names: list of names for each endmember. must match the number of lists passed.
        shade_normalize: flag to apply shade normalization during unmixing.

    Returns:
        unmixed: a 3-band image file in order of (soil-veg-impervious).
    """

    n_bands = len(list(img.bandNames().getInfo()))
    n_classes = len(endmembers)
    n_endmembers = len(endmembers[0])
    band_numbers = list(range(n_classes))
    shade = _ee.List([0] * n_bands)

    # create a list of images to append and later convert to an image collection
    unmixed = list()

    # loop through each iteration and unmix each
    for spectra in _tqdm(list(zip(*endmembers)), total=n_endmembers, desc="Unmixing"):

        if shade_normalize:
            spectra += (shade,)

        unmixed_iter = img.unmix(spectra, True, True).toFloat()

        # run the forward model to evaluate the fractional cover fit
        modeled_reflectance = computeModeledSpectra(spectra, unmixed_iter)
        rmse = computeSpectralRMSE(img, modeled_reflectance)

        # normalize by the observed shade fraction
        if shade_normalize:
            shade_fraction = unmixed_iter.select([n_classes]).subtract(1).abs()
            unmixed_iter = unmixed_iter.divide(shade_fraction)

        # rename the bands and append an rmse band
        unmixed.append(
            unmixed_iter.select(band_numbers, endmember_names).addBands(rmse)
        )

    # use the sum of rmse to weight each estimate
    rmse_sum = _ee.Image(
        _ee.ImageCollection.fromImages(unmixed)
        .select(["RMSE"])
        .sum()
        .select([0], ["SUM"])
        .toFloat()
    )
    unscaled = [computeWeight(fractions, rmse_sum) for fractions in unmixed]

    # use these weights to scale each unmixing estimate
    weight_sum = _ee.Image(
        _ee.ImageCollection.fromImages(unscaled).select(["weight"]).sum().toFloat()
    )
    scaled = [weightedAverage(fractions, weight_sum) for fractions in unscaled]

    # reduce it to a single image and return
    unmixed = _ee.ImageCollection.fromImages(scaled).sum().toFloat()

    return unmixed


def computeModeledSpectra(endmembers, fractions):
    """Constructs a modeled spectrum for each pixel based on endmember fractions.

    Args:
        endmembers: a list of _ee.List() items, each representing an endmember spectrum.
        fractions: ee.Image output from .unmix() with the same number of bands as items in `endmembers`.

    Returns:
        modeled_reflectance: an _ee.Image with n_bands equal to the number of endmember bands.
    """

    # compute the number of endmember bands
    nb = int(endmembers[0].length().getInfo())
    band_range = list(range(nb))
    band_names = [f"M{band:02d}" for band in band_range]

    # create a list to store each reflectance fraction
    refl_fraction_images = list()

    # loop through each endmember and mulitply the fraction estimated by the reflectance value
    for i, endmember in enumerate(endmembers):
        fraction = fractions.select([i])
        refl_fraction_list = [
            fraction.multiply(_ee.Image(endmember.get(band).getInfo()))
            for band in band_range
        ]
        refl_fraction_images.append(
            _ee.ImageCollection.fromImages(refl_fraction_list)
            .toBands()
            .select(band_range, band_names)
        )

    # convert these images to an image collection and sum them together to reconstruct the spectrum
    modeled_reflectance = (
        _ee.ImageCollection.fromImages(refl_fraction_images)
        .sum()
        .toFloat()
        .select(band_range, band_names)
    )

    return modeled_reflectance


def computeSpectralRMSE(measured, modeled):
    """Computes root mean squared error between measured and modeled spectra.

    Args:
        measured: an ee.Image of measured reflectance.
        modeled: an ee.Image of modeled reflectance.

    Returns:
        rmse: a floating point _ee.Image with pixel-wise RMSE values.
    """

    # harmonize band info to ensure element-wise computation
    band_names = list(measured.bandNames().getInfo())
    band_range = list(range(len(band_names)))

    # compute rmse
    rmse = (
        measured.select(band_range, band_names)
        .subtract(modeled.select(band_range, band_names))
        .pow(2)
        .reduce(_ee.Reducer.sum())
        .sqrt()
        .select([0], ["RMSE"])
        .toFloat()
    )

    return rmse


def computeWeight(fractions, rmse_sum):
    """Computes the relative weight for an image's RMSE based on the sum of the global RMSE.

    Args:
        fractions: a multi-band ee.Image object with an 'RMSE' band.
        rmse_sum: a single-band ee.Image object with the global RMSE value.

    Returns:
        unweighted: appends the fractions Image with a 'weight' band.
    """

    rmse = fractions.select(["RMSE"])
    ratio = rmse.divide(rmse_sum).toFloat().select([0], ["ratio"])
    weight = _ee.Image(1).subtract(ratio).select([0], ["weight"])
    unweighted = fractions.addBands([weight, ratio])

    return unweighted


def weightedAverage(fractions, weight_sum):
    """Computes an RMSE-weighted fractional cover image.

    Args:
        fractions: a multi-band ee.Image object with a 'weight' band.
        weight_sum: a single-band _eeImage object with the global weight sum.

    Returns:
        weighted: scaled fractional cover Image.
    """

    # harmonize band info
    band_names = list(fractions.bandNames().getInfo())
    band_names.pop(band_names.index("weight"))
    band_range = list(range(len(band_names)))

    scaler = fractions.select(["weight"]).divide(weight_sum)
    weighted = fractions.select(band_range, band_names).multiply(scaler)

    return weighted


def VIS(img, **normalization):
    """Unmixes according to the Vegetation-Impervious-Soil (VIS) approach.

    Args:
        img: the ee.Image to unmix.
        **normalization: keyword arguments to pass to fractionalCover(),
            like shade_normalize=True.

    Returns:
        unmixed: a 3-band image file in order of (soil-veg-impervious).
    """

    endmembers = [soil, pv, urban]
    endmember_names = ["soil", "pv", "impervious"]

    unmixed = fractionalCover(img, endmembers, endmember_names, **normalization)

    return unmixed


def SVN(img, **normalization):
    """Unmixes using Soil-Vegetation-NonphotosyntheticVegetation (SVN) endmembers.

    Args:
        img: the ee.Image to unmix.
        **normalization: keyword arguments to pass to fractionalCover(),
            like shade_normalize=True.

    Returns:
        unmixed: a 3-band image file in order of (soil-veg-npv).
    """

    endmembers = [soil, pv, npv]
    endmember_names = ["soil", "pv", "npv"]

    unmixed = fractionalCover(img, endmembers, endmember_names, **normalization)

    return unmixed


def BVN(img, **normalization):
    """Unmixes using Burned-Vegetation-NonphotosyntheticVegetation (BVN) endmembers.

    Args:
        img: the ee.Image to unmix.
    **normalization: keyword arguments to pass to fractionalCover(),
        like shade_normalize=True.

    Returns:
        unmixed: a 4-band image file in order of (burned-veg-npv-soil).
    """

    endmembers = [burn, pv, npv]
    endmember_names = ["burned", "pv", "npv"]

    unmixed = fractionalCover(img, endmembers, endmember_names, **normalization)

    return unmixed
