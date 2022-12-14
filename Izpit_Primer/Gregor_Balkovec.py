# Naloga 01
import math


def funkcija01(visina, radij):
    return math.pi*(radij**2)*visina


funkcija01(2, 3)

# Naloga 02


def funkcija02(l):
    passed_names = []
    for ocena, ime in l:
        #print(ocena, ime)
        if ocena >= 50:
            passed_names.append(ime)
    return passed_names

# Naloga 03


def funkcija03(data):
    best_perfomer_name = ""
    best_result = 0
    for coin, values in data["day_2"].items():
        percentage = (data["day_2"][coin]["eur"] - data["day_1"]
                      [coin]["eur"])/data["day_1"][coin]["eur"]
        print(f"{coin} se je spremenil za {percentage:.2f} %")
        if percentage > best_result:
            best_result = percentage
            best_performer_name = coin
    return best_performer_name


data = {
    "day_1": {
        "pivx": {
            "eur": 0.466608,
            "eur_market_cap": 31703850.28872451
        },
        "bitcoin": {
            "eur": 41653,
            "eur_market_cap": 789077487998.7858
        },
        "cardano": {
            "eur": 1.08,
            "eur_market_cap": 34819120071.59348
        },
        "polkadot": {
            "eur": 22.09,
            "eur_market_cap": 23660724367.996834
        },
        "ethereum": {
            "eur": 3382.92,
            "eur_market_cap": 403045423232.84467
        }
    },
    "day_2": {
        "bitcoin": {
            "eur": 43153,
            "eur_market_cap": 789077487998.7858
        },
        "pivx": {
            "eur": 0.365668,
            "eur_market_cap": 31703850.28872451
        },
        "polkadot": {
            "eur": 19.85,
            "eur_market_cap": 23660724367.996834
        },
        "ethereum": {
            "eur": 4624.21,
            "eur_market_cap": 403045423232.84467
        },
        "cardano": {
            "eur": 1.26,
            "eur_market_cap": 34819120071.59348
        },
    },

}
funkcija03(data)

# Naloga 04


# Rešitev
def funkcija04():
    with open("input_file.txt") as f:
        data = f.readlines()
        data = [line for line in data]
        data = [(len(line), line) for line in data]
        data.sort()

    with open("output_file.txt", "w") as f:
        for i, line in data:
            f.write(line)


funkcija04()

# Naloga 05

# Rešitev


class Planet:
    def __init__(self, ime, razdalja_od_sonca, masa):
        self.ime = ime
        self.razdalja_od_sonca = razdalja_od_sonca
        self.masa = masa

    def razdalja_od_planeta(self, drugi_planet):
        return abs(self.razdalja_od_sonca - drugi_planet.razdalja_od_sonca)


class Osoncje:
    def __init__(self, planeti=[]):
        self.planeti = planeti

    def dodaj_planet(self, planet):
        self.planeti.append(planet)

    def planet_z_najvecjo_maso(self):
        masa = 0
        ime = ""
        for planet in self.planeti:
            if planet.masa > masa:
                masa = planet.masa
                ime = planet.ime
        return ime

    def razvrsti_po_oddaljenosti(self):
        self.planeti.sort(key=lambda x: x.razdalja_od_sonca)

        razpored = [planet.ime for planet in self.planeti]
        return razpored
