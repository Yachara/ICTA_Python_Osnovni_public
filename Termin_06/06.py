class Pes:
    def __init__(self, name, age):
        self.ime = name
        self.starost = age

    def opis(self):
        print(f"{self.ime} je star {self.starost} let.")


fido = Pes("Fido", 9)
print(fido.ime, fido.starost)
fido.opis()

rex = Pes("Rex", 12)
print(rex.ime, rex.starost)
rex.opis()
