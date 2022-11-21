# Classes
# pes = {
#     "ime": "Fido",
#     "starost": 9,
#     "opis": opis_psa()
# }


# class Pes:
#     def __init__(self):
#         print("nov pes")
#         print(self)
#         self.ime = "Neki neki"


# fido = Pes()
# print(fido)
# print(fido.ime)

# rex = Pes()
# print(rex)


class Pes:
    def __init__(self, ime, starost):
        print("Ustvarili smo novega psa")
        self.starost = starost
        self.ime = ime


pes1 = Pes("Fido", 9)
print(pes1)
print(pes1.ime)
print(pes1.starost)

pes2 = Pes("Rex", 12)
print(pes2)
print(pes2.ime)
print(pes2.starost)
