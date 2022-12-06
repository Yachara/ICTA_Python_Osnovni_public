# Banka

# Napišite program:

class Oseba():
	def __init__(self, ime, priimek):
		# za to instanco naj ustvari spremenljivki ime in priimek
		self.ime = ime
		self.priimek = priimek
		
	def __str__(self):
		# vrne naj string, znotraj katerega imamo ime in priimek
		return f"{self.ime} {self.priimek}"

		
class Stranka(Oseba): # class naj deduje od razreda Oseba()
	def nastavi_stanje(self, stanje=0):
		# metoda naj ustvari spremenljivko samo za to instaco razreda.
		# Vrednost naj bo "stanje" oziroma default vrednost naj bo 0.
		self.stanje = stanje
		# Metoda naj nato vrne vrednost spremenljivke stanje
		return self.stanje

	def dvig(self, znesek):
		# Od stanja naj se odšteje znesek.
		# V kolikor ni dovolj denarja na računu naj se dvigne z banke celotno stanje
		# Na koncu naj metoda vrne dvignjen znesek
		if znesek<=self.stanje:
			self.stanje = self.stanje - znesek
			return znesek
		else:
			koliko_vzamemo_dol = self.stanje
			self.stanje = 0
			print(f"Dal ti bom samo {koliko_vzamemo_dol}")
			return koliko_vzamemo_dol

	def polog(self, znesek):
		# metoda naj doda velikost zneska stanju
		self.stanje = self.stanje + znesek
		# nato naj metoda vrne novo stanje
		return self.stanje

# INPUT:
objekt = Stranka("Gregor", "Balkovec")
print(objekt)
print(objekt.nastavi_stanje())
print(objekt.polog(5000))
print(objekt.dvig(2000))
print(objekt.dvig(4000))

# OUTPUT:
"""
Gregor Balkovec
0.0
5000.0
2000
Dal ti bom samo 3000.0
3000.0
"""

vse_strnke = [...]
vsea stanja = [...]

def dvig(stranka,stanje):
	pass