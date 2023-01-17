# Rešitev

data = {
    "TC": [
        {"ts": 1673748552,
        "value": 39},
        {"ts": 1673648552,
        "value": 36},
        {"ts": 1673548552,
        "value": 28},
        {"ts": 1673448552,
        "value": 23},
        {"ts": 1673348552,
        "value": 13},
    ],
    "HUM": [
        {"ts": 1673748552,
        "value": 12},
        {"ts": 1673648552,
        "value": 56},
        {"ts": 1673548552,
        "value": 86},
        {"ts": 1673448552,
        "value": 74},
        {"ts": 1673348552,
        "value": 23},
    ],
    "PRES": [
        {"ts": 1673748552,
        "value": 969},
        {"ts": 1673648552,
        "value": 957},
        {"ts": 1673548552,
        "value": 998},
        {"ts": 1673448552,
        "value": 1023},
        {"ts": 1673348552,
        "value": 989},
    ],
}

def funkcija03(d):
    prag = {
        "TC": 35,
        "HUM": 90,
        "PRES": 1000
    }
    for key, value in data.items():
        for measurment in value:
            if measurment["value"] > prag[key]:
                print(f"Preveri {key}. TS: {measurment['ts']}, VALUE: {measurment['value']}")
                break
            
funkcija03(data)