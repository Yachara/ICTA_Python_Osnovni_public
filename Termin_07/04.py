# Naloga:
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost 
# in kilometrino in koliko goriva je bilo porabljenega do sedaj.

# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba tega vozila.

# Dodajte class variable razredu Vozilo. Spremenljivki naj bo ime 
# st_gum in njena vrednost naj bo 4.
# Dodajte metodo opis(), ki naj izpiše opis vozila.

# Primeri:

# Input:
# avto = Vozilo("avto", 300, 80, 500)
# avto.opis()

# Output:
# Max hitrost avto: 300. Prevozenih je 80 km. Poraba vozila je 6.25. Vozilo ima 4 gum.

# Input:
# kamion = Vozilo("kamion", 90, 5500, 125000)
# print(f"Vozilo porabi {kamion.poraba()}l/km")

# Output:
# Max hitrost kamion: 180. Prevozenih je 5500 km. Poraba vozila je 22.727272727272727.


class Vozilo:

	st_gum = 4

	def __init__(self, tip1, hitrost1, kilometrina1, gorivo1):
		self.tip = tip1  # levo je spremenljivka instance, desno je atribut
		self.kilometrina = kilometrina1
		self.hitrost = hitrost1
		self.gorivo = gorivo1

	def poraba(self):
		return self.gorivo / self.kilometrina  # metoda lahko vrne vrednost

	def opis(self):
		# print(f"{self.tip} porabi {self.poraba()} l/km. Vozilo ima {self.st_gum} gume.")
		print(f"""Max hitrost avto: {self.hitrost}. Prevozenih \
je {self.kilometrina} km. Poraba vozila je {self.poraba()}. \
Vozilo ima {self.st_gum} gum.""")

avto = Vozilo("Avto", 300, 80, 500)
avto.opis()
