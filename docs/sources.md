# Data Sources

## Satellite instruments

<img src="img/supported-sensors.png" alt="earthlib satellite instrument">

The Earth Library is a collection of collections, merging spectral measurments and models from a range of raw data sources. `earthlib` provides routines for resampling this collection to match the wavelenghts of the sensors in the series above.


## Spectral Libraries

The following data sources were filtered and resampled prior to inclusion in `earthlib`.

- Vegetation spectra modeled using [PROSAIL](http://teledetection.ipgp.jussieu.fr/prosail/) (using [PyPROSAIL](https://pyprosail.readthedocs.io/en/latest/))
- World Agroforestry (ICRAF) Global [Soil Spectral Library](https://www.worldagroforestry.org/sd/landhealth/soil-plant-spectral-diagnostics-laboratory/soil-spectra-library)
- [The Joint Fire Science Program](https://www.frames.gov/assessing-burn-severity/spectral-library/overview)
- UCSB's [Urban Reflectance Spectra](https://ecosis.org/package/urban-reflectance-spectra-from-santa-barbara--ca)
- UW/BNL/NASA HySPIRI [airborne calibration spectra](https://ecosis.org/package/uw-bnl-nasa-hyspiri-airborne-campaign-leaf-and-canopy-spectra-and-trait-data)
- [USGS Spectral Library Version 7](https://www.sciencebase.gov/catalog/item/5807a2a2e4b0841e59e3a18d)

Below are plots for the primary groups of spectra included in `earthlib`.


### Photosynthetic vegetation

<img src="img/spectra-vegetation-mean-stdv.png" alt="earthlib photosynthetic vegetation spectra">

### Non-photosynthetic vegetation

<img src="img/spectra-npv-mean-stdv.png" alt="earthlib non-photosynthetic vegetation spectra">

### Bare ground

<img src="img/spectra-bare-mean-stdv.png" alt="earthlib bare ground spectra">

### Burned surfaces

<img src="img/spectra-burned-mean-stdv.png" alt="earthlib burned spectra">

### Built environment

<img src="img/spectra-urban-mean-stdv.png" alt="earthlib vegetation spectra">