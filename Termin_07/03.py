# spremenljivke razredov

class Pes:

	hrana = ["svinjina"]

	def __init__(self,ime,starost):
		self.ime = ime
		self.starost = starost
		# self.hrana_na_vljo_v_trgovini = ["svinjina"]
	
	def opis(self):
		print(f"{self.ime} je star {self.starost}.")

	def dodaj_hrano(self,nova_hrana):
		self.hrana.append(nova_hrana)


fido = Pes("Fido",9)
rex = Pes("Rex",10)

# fido.opis()
# rex.opis()

fido.dodaj_hrano("piščanec")
rex.hrana = ["briketi"]
Pes.hrana.append("mleko")
Pes.hrana = "nekaj_novega"

runo = Pes("Runo",7)

print(fido.hrana,id(fido.hrana))
print(rex.hrana,id(rex.hrana))
print(runo.hrana,id(runo.hrana))