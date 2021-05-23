"""A script to create a formatted json file with sensor/collection parameters."""

import json
import os

# set the output file path
script_path = os.path.realpath(__file__)
repo_directory = os.path.dirname(os.path.dirname(script_path))
output_path = os.path.join(repo_directory, "earthlib", "data", "collections.json")

# create the dictionary to write as json
collections = {
    # from http://www.gisagmaps.com/landsat-8-sentinel-2-bands/
    "Landsat8": {
        "collection": "LANDSAT/LC08/C01/T1_SR",
        "band_names": [
            "B2",
            "B3",
            "B4",
            "B5",
            "B6",
            "B7",
        ],
        "band_descriptions": [
            "blue",
            "green",
            "red",
            "near infrared",
            "shortwave infrared 1",
            "shortwave infrared 2",
        ],
        "band_centers": [0.482, 0.561, 0.655, 0.865, 1.609, 2.201],
        "band_widths": [0.060, 0.057, 0.037, 0.028, 0.085, 0.187],
        "scale": 0.0001,
    },
    # from http://www.gisagmaps.com/landsat-8-sentinel-2-bands/
    "Sentinel2": {
        "collection": "COPERNICUS/S2_SR",
        "band_names": [
            "B2",
            "B3",
            "B4",
            "B5",
            "B6",
            "B7",
            "B8",
            "B8A",
            "B11",
            "B12",
        ],
        "band_descriptions": [
            "blue",
            "green",
            "red",
            "red edge 1",
            "red edge 2",
            "red edge 3",
            "near infrared",
            "red edge 4",
            "shortwave infrared 1",
            "shortwave infrared 2",
        ],
        "band_centers": [
            0.494,
            0.560,
            0.665,
            0.704,
            0.740,
            0.781,
            0.834,
            0.864,
            1.612,
            2.194,
        ],
        "band_widths": [
            0.095,
            0.045,
            0.039,
            0.020,
            0.018,
            0.028,
            0.141,
            0.033,
            0.142,
            0.240,
        ],
        "scale": 0.0001,
    },
    "MODIS": {
        "collection": "MODIS/006/MOD09GA",
        "band_names": [
            "sur_refl_b03",
            "sur_refl_b04",
            "sur_refl_b01",
            "sur_refl_b02",
            "sur_refl_b05",
            "sur_refl_b06",
            "sur_refl_b07",
        ],
        "band_descriptions": [
            "blue",
            "green",
            "red",
            "near infrared",
            "near infrared 2",
            "shortwave infrared 1",
            "shortwave infrared 2",
        ],
        "band_centers": [
            0.469,
            0.555,
            0.645,
            0.858,
            1.240,
            1.640,
            2.130,
        ],
        "band_widths": [0.020, 0.020, 0.050, 0.035, 0.020, 0.024, 0.050],
        "scale": 0.0001,
    },
    "NEON": {
        "collection": None,
        "band_names": [
            "band_5",
            "band_6",
            "band_7",
            "band_8",
            "band_9",
            "band_10",
            "band_11",
            "band_12",
            "band_13",
            "band_14",
            "band_15",
            "band_16",
            "band_17",
            "band_18",
            "band_19",
            "band_20",
            "band_21",
            "band_22",
            "band_23",
            "band_24",
            "band_25",
            "band_26",
            "band_27",
            "band_28",
            "band_29",
            "band_30",
            "band_31",
            "band_32",
            "band_33",
            "band_34",
            "band_35",
            "band_36",
            "band_37",
            "band_38",
            "band_39",
            "band_40",
            "band_41",
            "band_42",
            "band_43",
            "band_44",
            "band_45",
            "band_46",
            "band_47",
            "band_48",
            "band_49",
            "band_50",
            "band_51",
            "band_52",
            "band_53",
            "band_54",
            "band_55",
            "band_56",
            "band_57",
            "band_58",
            "band_59",
            "band_60",
            "band_61",
            "band_62",
            "band_63",
            "band_64",
            "band_65",
            "band_66",
            "band_67",
            "band_68",
            "band_69",
            "band_70",
            "band_71",
            "band_72",
            "band_73",
            "band_74",
            "band_75",
            "band_76",
            "band_77",
            "band_78",
            "band_79",
            "band_80",
            "band_81",
            "band_82",
            "band_83",
            "band_84",
            "band_85",
            "band_86",
            "band_87",
            "band_88",
            "band_89",
            "band_90",
            "band_91",
            "band_92",
            "band_93",
            "band_94",
            "band_95",
            "band_96",
            "band_97",
            "band_98",
            "band_99",
            "band_100",
            "band_101",
            "band_102",
            "band_103",
            "band_104",
            "band_105",
            "band_106",
            "band_107",
            "band_108",
            "band_109",
            "band_110",
            "band_111",
            "band_112",
            "band_113",
            "band_114",
            "band_115",
            "band_116",
            "band_117",
            "band_118",
            "band_119",
            "band_120",
            "band_121",
            "band_122",
            "band_123",
            "band_124",
            "band_125",
            "band_126",
            "band_127",
            "band_128",
            "band_129",
            "band_130",
            "band_131",
            "band_132",
            "band_133",
            "band_134",
            "band_135",
            "band_136",
            "band_137",
            "band_138",
            "band_139",
            "band_140",
            "band_141",
            "band_142",
            "band_143",
            "band_144",
            "band_145",
            "band_146",
            "band_147",
            "band_148",
            "band_149",
            "band_150",
            "band_151",
            "band_152",
            "band_153",
            "band_154",
            "band_155",
            "band_156",
            "band_157",
            "band_158",
            "band_159",
            "band_160",
            "band_161",
            "band_162",
            "band_163",
            "band_164",
            "band_165",
            "band_166",
            "band_167",
            "band_168",
            "band_169",
            "band_170",
            "band_171",
            "band_172",
            "band_173",
            "band_174",
            "band_175",
            "band_176",
            "band_177",
            "band_178",
            "band_179",
            "band_180",
            "band_181",
            "band_182",
            "band_183",
            "band_184",
            "band_185",
            "band_186",
            "band_187",
            "band_188",
            "band_189",
            "band_190",
            "band_191",
            "band_192",
            "band_193",
            "band_194",
            "band_195",
            "band_196",
            "band_197",
            "band_198",
            "band_199",
            "band_200",
            "band_210",
            "band_211",
            "band_212",
            "band_213",
            "band_214",
            "band_215",
            "band_216",
            "band_217",
            "band_218",
            "band_219",
            "band_220",
            "band_221",
            "band_222",
            "band_223",
            "band_224",
            "band_225",
            "band_226",
            "band_227",
            "band_228",
            "band_229",
            "band_230",
            "band_231",
            "band_232",
            "band_233",
            "band_234",
            "band_235",
            "band_236",
            "band_237",
            "band_238",
            "band_239",
            "band_240",
            "band_241",
            "band_242",
            "band_243",
            "band_244",
            "band_245",
            "band_246",
            "band_247",
            "band_248",
            "band_249",
            "band_250",
            "band_251",
            "band_252",
            "band_253",
            "band_254",
            "band_255",
            "band_256",
            "band_257",
            "band_258",
            "band_259",
            "band_260",
            "band_261",
            "band_262",
            "band_263",
            "band_264",
            "band_265",
            "band_266",
            "band_267",
            "band_268",
            "band_269",
            "band_270",
            "band_271",
            "band_272",
            "band_273",
            "band_274",
            "band_275",
            "band_276",
            "band_277",
            "band_278",
            "band_279",
            "band_280",
            "band_281",
            "band_282",
            "band_283",
            "band_284",
            "band_285",
            "band_286",
            "band_287",
            "band_288",
            "band_289",
            "band_290",
            "band_291",
            "band_307",
            "band_308",
            "band_309",
            "band_310",
            "band_311",
            "band_312",
            "band_313",
            "band_314",
            "band_315",
            "band_316",
            "band_317",
            "band_318",
            "band_319",
            "band_320",
            "band_321",
            "band_322",
            "band_323",
            "band_324",
            "band_325",
            "band_326",
            "band_327",
            "band_328",
            "band_329",
            "band_330",
            "band_331",
            "band_332",
            "band_333",
            "band_334",
            "band_335",
            "band_336",
            "band_337",
            "band_338",
            "band_339",
            "band_340",
            "band_341",
            "band_342",
            "band_343",
            "band_344",
            "band_345",
            "band_346",
            "band_347",
            "band_348",
            "band_349",
            "band_350",
            "band_351",
            "band_352",
            "band_353",
            "band_354",
            "band_355",
            "band_356",
            "band_357",
            "band_358",
            "band_359",
            "band_360",
            "band_361",
            "band_362",
            "band_363",
            "band_364",
            "band_365",
            "band_366",
            "band_367",
            "band_368",
            "band_369",
            "band_370",
            "band_371",
            "band_372",
            "band_373",
            "band_374",
            "band_375",
            "band_376",
            "band_377",
            "band_378",
            "band_379",
            "band_380",
            "band_381",
            "band_382",
            "band_383",
            "band_384",
            "band_385",
            "band_386",
            "band_387",
            "band_388",
            "band_389",
            "band_390",
            "band_391",
            "band_392",
            "band_393",
            "band_394",
            "band_395",
            "band_396",
            "band_397",
            "band_398",
            "band_399",
            "band_400",
            "band_401",
            "band_402",
            "band_403",
            "band_404",
            "band_405",
            "band_406",
            "band_407",
            "band_408",
            "band_409",
            "band_410",
            "band_411",
            "band_412",
            "band_413",
        ],
        "band_descriptions": [
            "band_5",
            "band_6",
            "band_7",
            "band_8",
            "band_9",
            "band_10",
            "band_11",
            "band_12",
            "band_13",
            "band_14",
            "band_15",
            "band_16",
            "band_17",
            "band_18",
            "band_19",
            "band_20",
            "band_21",
            "band_22",
            "band_23",
            "band_24",
            "band_25",
            "band_26",
            "band_27",
            "band_28",
            "band_29",
            "band_30",
            "band_31",
            "band_32",
            "band_33",
            "band_34",
            "band_35",
            "band_36",
            "band_37",
            "band_38",
            "band_39",
            "band_40",
            "band_41",
            "band_42",
            "band_43",
            "band_44",
            "band_45",
            "band_46",
            "band_47",
            "band_48",
            "band_49",
            "band_50",
            "band_51",
            "band_52",
            "band_53",
            "band_54",
            "band_55",
            "band_56",
            "band_57",
            "band_58",
            "band_59",
            "band_60",
            "band_61",
            "band_62",
            "band_63",
            "band_64",
            "band_65",
            "band_66",
            "band_67",
            "band_68",
            "band_69",
            "band_70",
            "band_71",
            "band_72",
            "band_73",
            "band_74",
            "band_75",
            "band_76",
            "band_77",
            "band_78",
            "band_79",
            "band_80",
            "band_81",
            "band_82",
            "band_83",
            "band_84",
            "band_85",
            "band_86",
            "band_87",
            "band_88",
            "band_89",
            "band_90",
            "band_91",
            "band_92",
            "band_93",
            "band_94",
            "band_95",
            "band_96",
            "band_97",
            "band_98",
            "band_99",
            "band_100",
            "band_101",
            "band_102",
            "band_103",
            "band_104",
            "band_105",
            "band_106",
            "band_107",
            "band_108",
            "band_109",
            "band_110",
            "band_111",
            "band_112",
            "band_113",
            "band_114",
            "band_115",
            "band_116",
            "band_117",
            "band_118",
            "band_119",
            "band_120",
            "band_121",
            "band_122",
            "band_123",
            "band_124",
            "band_125",
            "band_126",
            "band_127",
            "band_128",
            "band_129",
            "band_130",
            "band_131",
            "band_132",
            "band_133",
            "band_134",
            "band_135",
            "band_136",
            "band_137",
            "band_138",
            "band_139",
            "band_140",
            "band_141",
            "band_142",
            "band_143",
            "band_144",
            "band_145",
            "band_146",
            "band_147",
            "band_148",
            "band_149",
            "band_150",
            "band_151",
            "band_152",
            "band_153",
            "band_154",
            "band_155",
            "band_156",
            "band_157",
            "band_158",
            "band_159",
            "band_160",
            "band_161",
            "band_162",
            "band_163",
            "band_164",
            "band_165",
            "band_166",
            "band_167",
            "band_168",
            "band_169",
            "band_170",
            "band_171",
            "band_172",
            "band_173",
            "band_174",
            "band_175",
            "band_176",
            "band_177",
            "band_178",
            "band_179",
            "band_180",
            "band_181",
            "band_182",
            "band_183",
            "band_184",
            "band_185",
            "band_186",
            "band_187",
            "band_188",
            "band_189",
            "band_190",
            "band_191",
            "band_192",
            "band_193",
            "band_194",
            "band_195",
            "band_196",
            "band_197",
            "band_198",
            "band_199",
            "band_200",
            "band_210",
            "band_211",
            "band_212",
            "band_213",
            "band_214",
            "band_215",
            "band_216",
            "band_217",
            "band_218",
            "band_219",
            "band_220",
            "band_221",
            "band_222",
            "band_223",
            "band_224",
            "band_225",
            "band_226",
            "band_227",
            "band_228",
            "band_229",
            "band_230",
            "band_231",
            "band_232",
            "band_233",
            "band_234",
            "band_235",
            "band_236",
            "band_237",
            "band_238",
            "band_239",
            "band_240",
            "band_241",
            "band_242",
            "band_243",
            "band_244",
            "band_245",
            "band_246",
            "band_247",
            "band_248",
            "band_249",
            "band_250",
            "band_251",
            "band_252",
            "band_253",
            "band_254",
            "band_255",
            "band_256",
            "band_257",
            "band_258",
            "band_259",
            "band_260",
            "band_261",
            "band_262",
            "band_263",
            "band_264",
            "band_265",
            "band_266",
            "band_267",
            "band_268",
            "band_269",
            "band_270",
            "band_271",
            "band_272",
            "band_273",
            "band_274",
            "band_275",
            "band_276",
            "band_277",
            "band_278",
            "band_279",
            "band_280",
            "band_281",
            "band_282",
            "band_283",
            "band_284",
            "band_285",
            "band_286",
            "band_287",
            "band_288",
            "band_289",
            "band_290",
            "band_291",
            "band_307",
            "band_308",
            "band_309",
            "band_310",
            "band_311",
            "band_312",
            "band_313",
            "band_314",
            "band_315",
            "band_316",
            "band_317",
            "band_318",
            "band_319",
            "band_320",
            "band_321",
            "band_322",
            "band_323",
            "band_324",
            "band_325",
            "band_326",
            "band_327",
            "band_328",
            "band_329",
            "band_330",
            "band_331",
            "band_332",
            "band_333",
            "band_334",
            "band_335",
            "band_336",
            "band_337",
            "band_338",
            "band_339",
            "band_340",
            "band_341",
            "band_342",
            "band_343",
            "band_344",
            "band_345",
            "band_346",
            "band_347",
            "band_348",
            "band_349",
            "band_350",
            "band_351",
            "band_352",
            "band_353",
            "band_354",
            "band_355",
            "band_356",
            "band_357",
            "band_358",
            "band_359",
            "band_360",
            "band_361",
            "band_362",
            "band_363",
            "band_364",
            "band_365",
            "band_366",
            "band_367",
            "band_368",
            "band_369",
            "band_370",
            "band_371",
            "band_372",
            "band_373",
            "band_374",
            "band_375",
            "band_376",
            "band_377",
            "band_378",
            "band_379",
            "band_380",
            "band_381",
            "band_382",
            "band_383",
            "band_384",
            "band_385",
            "band_386",
            "band_387",
            "band_388",
            "band_389",
            "band_390",
            "band_391",
            "band_392",
            "band_393",
            "band_394",
            "band_395",
            "band_396",
            "band_397",
            "band_398",
            "band_399",
            "band_400",
            "band_401",
            "band_402",
            "band_403",
            "band_404",
            "band_405",
            "band_406",
            "band_407",
            "band_408",
            "band_409",
            "band_410",
            "band_411",
            "band_412",
            "band_413",
        ],
        "band_centers": [
            0.4027,
            0.4077,
            0.4127,
            0.4177,
            0.4227,
            0.4277,
            0.4328,
            0.4378,
            0.4428,
            0.4478,
            0.4528,
            0.4578,
            0.4628,
            0.4678,
            0.4728,
            0.4778,
            0.4829,
            0.4879,
            0.4929,
            0.4979,
            0.5029,
            0.5079,
            0.5129,
            0.5179,
            0.5229,
            0.5279,
            0.5329,
            0.5379,
            0.5429,
            0.5479,
            0.5529,
            0.5579,
            0.563,
            0.568,
            0.573,
            0.578,
            0.5831,
            0.5881,
            0.5931,
            0.5981,
            0.6031,
            0.6081,
            0.6131,
            0.6181,
            0.6231,
            0.6281,
            0.6331,
            0.6381,
            0.6432,
            0.6482,
            0.6532,
            0.6582,
            0.6632,
            0.6682,
            0.6732,
            0.6782,
            0.6832,
            0.6883,
            0.6933,
            0.6983,
            0.7033,
            0.7083,
            0.7133,
            0.7183,
            0.7233,
            0.7283,
            0.7333,
            0.7383,
            0.7434,
            0.7484,
            0.7534,
            0.7584,
            0.7634,
            0.7684,
            0.7734,
            0.7784,
            0.7834,
            0.7884,
            0.7934,
            0.7985,
            0.8035,
            0.8085,
            0.8135,
            0.8185,
            0.8235,
            0.8285,
            0.8335,
            0.8385,
            0.8435,
            0.8486,
            0.8536,
            0.8586,
            0.8636,
            0.8686,
            0.8736,
            0.8786,
            0.8836,
            0.8886,
            0.8936,
            0.8986,
            0.9037,
            0.9087,
            0.9137,
            0.9187,
            0.9237,
            0.9287,
            0.9337,
            0.9387,
            0.9437,
            0.9487,
            0.9538,
            0.9588,
            0.9638,
            0.9688,
            0.9738,
            0.9788,
            0.9838,
            0.9888,
            0.9938,
            0.9988,
            1.0038,
            1.0089,
            1.0139,
            1.0189,
            1.0239,
            1.0289,
            1.0339,
            1.0389,
            1.0439,
            1.0489,
            1.0539,
            1.0589,
            1.064,
            1.069,
            1.074,
            1.079,
            1.084,
            1.089,
            1.094,
            1.099,
            1.104,
            1.1091,
            1.1141,
            1.1191,
            1.1241,
            1.1291,
            1.1341,
            1.1391,
            1.1441,
            1.1491,
            1.1541,
            1.1591,
            1.1642,
            1.1692,
            1.1742,
            1.1792,
            1.1842,
            1.1892,
            1.1942,
            1.1992,
            1.2042,
            1.2092,
            1.2142,
            1.2193,
            1.2243,
            1.2293,
            1.2343,
            1.2393,
            1.2443,
            1.2493,
            1.2543,
            1.2593,
            1.2643,
            1.2694,
            1.2744,
            1.2794,
            1.2844,
            1.2894,
            1.2944,
            1.2994,
            1.3044,
            1.3094,
            1.3144,
            1.3195,
            1.3245,
            1.3295,
            1.3345,
            1.3395,
            1.3445,
            1.3495,
            1.3545,
            1.3595,
            1.3645,
            1.3695,
            1.3745,
            1.3796,
            1.4296,
            1.4347,
            1.4397,
            1.4447,
            1.4497,
            1.4547,
            1.4597,
            1.4647,
            1.4697,
            1.4747,
            1.4798,
            1.4848,
            1.4898,
            1.4948,
            1.4998,
            1.5048,
            1.5098,
            1.5148,
            1.5198,
            1.5248,
            1.5298,
            1.5349,
            1.5399,
            1.5449,
            1.5499,
            1.5549,
            1.5599,
            1.5649,
            1.5699,
            1.5749,
            1.5799,
            1.5849,
            1.59,
            1.595,
            1.6,
            1.605,
            1.61,
            1.615,
            1.62,
            1.625,
            1.63,
            1.635,
            1.6401,
            1.6451,
            1.6501,
            1.6551,
            1.6601,
            1.6651,
            1.6701,
            1.6751,
            1.6801,
            1.6851,
            1.6902,
            1.6952,
            1.7002,
            1.7052,
            1.7102,
            1.7152,
            1.7202,
            1.7252,
            1.7302,
            1.7352,
            1.7402,
            1.7452,
            1.7503,
            1.7553,
            1.7603,
            1.7653,
            1.7703,
            1.7753,
            1.7803,
            1.7853,
            1.7903,
            1.7953,
            1.8004,
            1.8054,
            1.8104,
            1.8154,
            1.8204,
            1.8254,
            1.8304,
            1.8354,
            1.9156,
            1.9206,
            1.9256,
            1.9306,
            1.9356,
            1.9406,
            1.9456,
            1.9506,
            1.9556,
            1.9607,
            1.9657,
            1.9707,
            1.9757,
            1.9807,
            1.9857,
            1.9907,
            1.9957,
            2.0007,
            2.0057,
            2.0108,
            2.0158,
            2.0208,
            2.0258,
            2.0308,
            2.0358,
            2.0408,
            2.0458,
            2.0508,
            2.0558,
            2.0608,
            2.0659,
            2.0709,
            2.0759,
            2.0809,
            2.0859,
            2.0909,
            2.0959,
            2.1009,
            2.1059,
            2.1109,
            2.116,
            2.121,
            2.126,
            2.131,
            2.136,
            2.141,
            2.146,
            2.151,
            2.156,
            2.161,
            2.166,
            2.1711,
            2.1761,
            2.1811,
            2.1861,
            2.1911,
            2.1961,
            2.2011,
            2.2061,
            2.2111,
            2.2162,
            2.2212,
            2.2262,
            2.2312,
            2.2362,
            2.2412,
            2.2462,
            2.2512,
            2.2562,
            2.2612,
            2.2662,
            2.2713,
            2.2763,
            2.2813,
            2.2863,
            2.2913,
            2.2963,
            2.3013,
            2.3063,
            2.3113,
            2.3163,
            2.3214,
            2.3264,
            2.3314,
            2.3364,
            2.3414,
            2.3464,
            2.3514,
            2.3564,
            2.3614,
            2.3664,
            2.3714,
            2.3765,
            2.3815,
            2.3865,
            2.3915,
            2.3965,
            2.4015,
            2.4065,
            2.4115,
            2.4165,
            2.4215,
            2.4265,
            2.4316,
            2.4366,
            2.4416,
            2.4466,
        ],
        "band_widths": [
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
            0.0075,
        ],
        "scale": 0.0001,
    },
}


# write the output file
with open(output_path, "w+") as f:
    f.write(json.dumps(collections, indent=2, sort_keys=True))
