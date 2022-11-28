# Naloga: 
# Ustvarite razred Vozilo. Vsaka instanca naj ima svojo specifično hitrost in 
# kilometrino in koliko goriva je bilo porabljenega do sedaj. 
# 
# Razred Vozilo naj ima funkcija poraba(), ki vrne koliko je povprečna poraba tega vozila.
# 
# Dodajte class variable razredu Vozilo. Spremenljivki naj bo ime st_gum 
# in njena vrednost naj bo 4. 
# 
# Dodajte metodo opis(), ki naj izpiše opis vozila.
# 
# Ustvarite podrazreda Avto in Motor. Razreda naj dedujete od razreda Vozila. 
# Motor razred naj prepiše spremenljivko st_gum v 2. Vsak razred naj pravilno 
# shrani ime vozila, ko ustvarimo novo instanco.
# 
class Vozilo:

	st_gum = 4

	def __init__(self, tip1, hitrost1, kilometrina1, gorivo1):
		self.tip = tip1  # levo je spremenljivka instance, desno je atribut
		self.kilometrina = kilometrina1
		self.hitrost = hitrost1
		self.gorivo = gorivo1

	def poraba(self):
		return round(self.gorivo / self.kilometrina,2)  # metoda lahko vrne vrednost

	def opis(self):
		# print(f"{self.tip} porabi {self.poraba()} l/km. Vozilo ima {self.st_gum} gume.")
		print(f"""Max hitrost {self.tip}: {self.hitrost}. Prevozenih \
je {self.kilometrina} km. Poraba vozila je {self.poraba()} l/km. \
Vozilo ima {self.st_gum} gum.""")



class Avto(Vozilo):
	def __init__(self, hitrost1, kilometrina1, gorivo1):
		super().__init__("avto", hitrost1, kilometrina1, gorivo1)

class Motor(Vozilo):
	st_gum = 2
	def __init__(self, hitrost1, kilometrina1, gorivo1):
		super().__init__("motor", hitrost1, kilometrina1, gorivo1)


# Primeri:

# Input: 
avto = Avto(300, 80, 500) 
avto.opis() 
# 
# Output: Max hitrost avto: 300. Prevozenih je 80 km. Poraba vozila je 6.25 l/km. Vozilo ima 4 gum.
# 
# Input: 
motor = Motor(90, 220, 520) 
motor.opis() 
# 
# Output: 
# Max hitrost motor: 90. Prevozenih je 220 km. Poraba vozila je 2.36 l/km. Vozilo ima 2 gum. 
