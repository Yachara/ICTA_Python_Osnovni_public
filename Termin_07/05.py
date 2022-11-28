# dedovanje (class inheritance) razreda

class Pes:
	vrsta = "pes"
	hrana = ["svinjina"]

	def __init__(self,ime,starost):
		self.ime = ime
		self.starost = starost
	
	def opis(self):
		return f"{self.ime} je star {self.starost}."

	def spremeni_vrsto(self,vrsta):
		self.vrsta = vrsta
	
	def dodaj_hrano(self,hrana):
		self.hrana.append(hrana)

fido = Pes("Fido",9)
# print(fido.opis())

# class Bulldog(Pes):
# 	pass

# # print(Bulldog.vrsta,Bulldog.hrana)
# spencer = Bulldog("Spencer",15)

# print(type(fido))
# print(type(spencer))

# print(spencer.opis())



# print("-"*10)

class Bulldog(Pes):
	
	hrana = ["piščanec"]

	def __init__(self,ime, starost, najljubsa_hrana):
		super().__init__(ime,starost)
		self.najljubsa_hrana = najljubsa_hrana

	def bark(self):
		print("Woof, woof.")
	
	def opis(self):
		return f"{self.ime} je star {self.starost} in je pasme Bulldog. Najraje je {self.najljubsa_hrana}"

spencer = Bulldog("Spencer",9, "čevapi")
fido = Pes("Fido",7)
# spencer.bark()
# fido.bark()

print(type(spencer),spencer.opis())
print(type(fido),fido.opis())

# print(Bulldog.hrana)
# print(Pes.hrana)
# print(spencer.super().opis()) # vrne napaka





