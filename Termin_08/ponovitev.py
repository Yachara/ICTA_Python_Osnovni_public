# povezava do spletne datoteke za hitro izmenjavo besedila (oba linka peljea na isto spletno stran)

# https://kody.js.org/#-NIXo1tGJ2RpCw72_A_Y
# shorturl.at/nuLS9

class Pes:
	hrana = ["piščanec"]
	def __init__(self,ime):
		self.ime = ime
	def opis_psa(self):
		print(f"Psu je ime {self.ime}.")
	def dolzina_imena(self):
		return len(self.ime)

rex = Pes("Rex")
rex.opis_psa()
print(rex.dolzina_imena())

print()
print(Pes.hrana)
print(rex.hrana)
rex.hrana.append("briketi")
rex.hrana = ["klobasa"]
print(Pes.hrana)
print(rex.hrana)


Pes.hrana = "nič"
print(Pes.hrana)
print(rex.hrana)


class Bulldog(Pes):
	pasma = "bulldog"
	def opis_psa(self):
		super().opis_psa()
		print(f"Psu je ime {self.ime} in je pasme {self.pasma}.")

floki = Bulldog("Floki")
print()
rex.opis_psa()
floki.opis_psa()



class A:
	temp = 1
	def fun(self):
		return 100
class B:
	temp = 2
	def fun(self):
		return 200
class C(A,B):
	pass

t = C()
print()
print(t.temp)
print(t.fun())


class Nivo1:
	temp = 1
class Nivo2(Nivo1):
	temp = 2
class Nivo3(Nivo2):
	pass

t = Nivo3()
print()
print(t.temp)
