# shorturl.at/cvyVY
# https://collabedit.com/q2gkk


# Naloga:
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost 
# in kilometrino in koliko goriva je bilo porabljenega do sedaj.
# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna 
# poraba tega vozila.

# Primeri:

# Input:
# avto = Vozilo("avto", 300, 80, 100)
# print(avto.poraba())

# Output:
# Vozilo porabi 6.25 l/km

# Input:
# kamion = Vozilo("kamion", 90, 5500, 125000)
# print(f"Vozilo porabi {kamion.poraba()} l/km")

# Output:
# Vozilo porabi 22.73 l/km

class Vozilo:
	def __init__(self, tip1, hitrost1, kilometrina1, gorivo1):
		self.tip = tip1
		self.kilometrina = kilometrina1
		self.hitrost = hitrost1
		self.gorivo = gorivo1

	def poraba(self):
		return self.gorivo/self.kilometrina
	



# Input:
avto = Vozilo("avto", 300, 80, 100)
print(avto.poraba())

# Input:
kamion = Vozilo("kamion", 90, 5500, 125000)
print(f"Vozilo porabi {kamion.poraba()} l/km.")






