# shorturl.at/bfATU


"""
Imamo podatke o GDP Evropskih držav od 
leta 2010 do 2020.
Uporabite funkcijo sorted() 
in določite takšno lambda funkcijo,
 da razvrstimo države po GDP 
 leta 2020 od največje do najmanjše.

Izpišite imena držav od največje do najmanjše.

Output:
Germany
United Kingdom
France
Italy
Spain
Netherlands
Switzerland
Turkey
Poland
Sweden
Belgium
Austria
Ireland
Norway
Denmark
Finland
Romania
Czech Republic
Portugal
Greece
Hungary
Slovakia
Luxembourg
Bulgaria
Croatia
Lithuania
Serbia
Slovenia
Latvia
Estonia
Cyprus
Iceland
Bosnia
Malta
Liechtenstein
Montenegro
"""

data = [
    [
        "Austria",
        392.623,
        431.515,
        409.652,
        430.203,
        442.698,
        381.998,
        394.215,
        417.721,
        456.166,
        447.718,
        432.894,
    ],
    [
        "Belgium",
        484.450,
        527.492,
        498.161,
        521.090,
        531.651,
        456.067,
        469.931,
        495.953,
        532.268,
        517.609,
        503.416,
    ],
    [
        "Bosnia",
        17.164,
        18.629,
        17.207,
        18.155,
        18.522,
        16.210,
        16.910,
        18.081,
        20.162,
        20.106,
        18.893,
    ],
    [
        "Bulgaria",
        50.611,
        57.420,
        53.901,
        55.557,
        56.815,
        50.201,
        53.236,
        58.342,
        65.197,
        66.250,
        67.917,
    ],
    [
        "Croatia",
        59.866,
        62.399,
        56.549,
        58.158,
        57.683,
        49.519,
        51.623,
        55.201,
        60.805,
        60.702,
        56.768,
    ],
    [
        "Cyprus",
        25.608,
        27.454,
        25.055,
        24.094,
        23.401,
        19.691,
        20.461,
        22.189,
        24.493,
        24.280,
        23.246,
    ],
    [
        "Czech Republic",
        207.478,
        227.948,
        207.376,
        209.402,
        207.818,
        186.830,
        195.090,
        215.914,
        245.226,
        246.953,
        241.975,
    ],
    [
        "Denmark",
        321.995,
        344.003,
        327.149,
        343.584,
        352.994,
        302.673,
        311.988,
        329.866,
        352.058,
        347.176,
        339.626,
    ],
    [
        "Estonia",
        19.536,
        23.191,
        23.057,
        25.145,
        26.658,
        22.916,
        23.994,
        26.850,
        30.761,
        31.038,
        30.468,
    ],
    [
        "Finland",
        248.262,
        273.925,
        256.849,
        270.065,
        273.042,
        232.582,
        239.150,
        252.867,
        274.210,
        269.654,
        267.856,
    ],
    [
        "France",
        2647.537,
        2864.030,
        2685.311,
        2811.957,
        2856.697,
        2439.435,
        2466.152,
        2591.775,
        2780.152,
        2707.074,
        2551.451,
    ],
    [
        "Germany",
        3423.466,
        3761.142,
        3545.946,
        3753.687,
        3904.921,
        3383.091,
        3496.606,
        3664.511,
        3951.340,
        3863.344,
        3780.553,
    ],
    [
        "Greece",
        299.919,
        288.062,
        245.807,
        239.937,
        237.406,
        196.690,
        195.303,
        203.493,
        218.230,
        214.012,
        194.376,
    ],
    [
        "Hungary",
        130.923,
        140.782,
        127.857,
        135.221,
        140.083,
        123.074,
        126.008,
        139.844,
        161.182,
        170.407,
        149.939,
    ],
    [
        "Iceland",
        13.684,
        15.159,
        14.724,
        16.034,
        17.758,
        17.389,
        20.618,
        24.457,
        25.965,
        23.918,
        20.805,
    ],
    [
        "Ireland",
        222.533,
        238.088,
        225.140,
        238.708,
        259.200,
        290.858,
        301.968,
        335.211,
        382.754,
        384.940,
        399.064,
    ],
    [
        "Italy",
        2129.021,
        2278.376,
        2073.971,
        2131.159,
        2155.151,
        1833.195,
        1869.973,
        1950.703,
        2075.856,
        2001.440,
        1848.222,
    ],
    [
        "Latvia",
        23.809,
        28.496,
        28.141,
        30.260,
        31.385,
        26.986,
        27.707,
        30.528,
        34.882,
        35.045,
        33.015,
    ],
    [
        "Lithuania",
        37.200,
        43.564,
        42.887,
        46.423,
        48.632,
        41.538,
        42.991,
        47.645,
        53.302,
        53.641,
        55.064,
    ],
    [
        "Luxembourg",
        53.312,
        60.060,
        56.709,
        61.759,
        66.209,
        57.233,
        58.985,
        62.449,
        69.553,
        69.453,
        68.613,
    ],
    [
        "Malta",
        8.757,
        9.511,
        9.215,
        10.154,
        11.302,
        10.701,
        11.446,
        12.764,
        14.560,
        14.859,
        14.290,
    ],
    [
        "Montenegro",
        4.147,
        4.543,
        4.090,
        4.466,
        4.595,
        4.055,
        4.376,
        4.855,
        5.457,
        5.424,
        4.943,
    ],
    [
        "Netherlands",
        848.133,
        904.915,
        839.436,
        877.198,
        892.397,
        765.650,
        783.852,
        833.575,
        914.519,
        902.355,
        886.339,
    ],
    [
        "Norway",
        429.131,
        498.832,
        510.229,
        523.502,
        499.338,
        386.663,
        371.345,
        398.394,
        434.167,
        417.627,
        366.386,
    ],
    [
        "Poland",
        479.161,
        528.571,
        500.846,
        524.399,
        545.284,
        477.568,
        471.843,
        526.749,
        585.816,
        565.854,
        580.894,
    ],
    [
        "Portugal",
        238.748,
        245.119,
        216.488,
        226.144,
        229.995,
        199.521,
        206.361,
        221.280,
        240.901,
        236.408,
        221.716,
    ],
    [
        "Romania",
        166.225,
        183.443,
        171.196,
        190.948,
        199.628,
        177.895,
        188.495,
        211.407,
        239.552,
        243.698,
        248.624,
    ],
    [
        "Serbia",
        41.369,
        49.280,
        43.300,
        48.394,
        47.062,
        39.629,
        40.630,
        44.120,
        50.509,
        51.523,
        51.999,
    ],
    [
        "Slovakia",
        89.668,
        98.271,
        93.466,
        98.509,
        101.109,
        87.814,
        89.885,
        95.821,
        106.573,
        106.552,
        101.892,
    ],
    [
        "Slovenia",
        48.103,
        51.338,
        46.378,
        48.131,
        49.969,
        43.124,
        44.660,
        48.545,
        54.059,
        54.154,
        51.802,
    ],
    [
        "Spain",
        1434.286,
        1489.431,
        1336.759,
        1362.280,
        1379.098,
        1199.688,
        1238.010,
        1317.104,
        1427.533,
        1397.870,
        1247.464,
    ],
    [
        "Sweden",
        488.909,
        563.797,
        544.482,
        579.361,
        574.413,
        498.118,
        512.205,
        540.545,
        556.073,
        528.929,
        529.054,
    ],
    [
        "Switzerland",
        583.053,
        699.670,
        667.890,
        688.747,
        709.496,
        679.721,
        670.247,
        680.029,
        705.546,
        715.360,
        707.868,
    ],
    [
        "Turkey",
        772.290,
        832.497,
        873.696,
        950.328,
        934.075,
        859.449,
        863.390,
        852.648,
        771.274,
        743.708,
        649.436,
    ],
    [
        "United Kingdom",
        2455.309,
        2635.799,
        2677.082,
        2755.356,
        3036.310,
        2897.060,
        2669.107,
        2640.067,
        2828.833,
        2743.586,
        2638.296,
    ],
]


data_sorted = sorted(data, key=lambda x: x[-1], reverse=True)
for i in data_sorted:
    print(i[0])
