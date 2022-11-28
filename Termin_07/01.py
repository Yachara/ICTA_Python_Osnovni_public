# naloge z nizi (Stringi)

# vislice


class Pes:
	def __init__(self,ime):
		# print(self)
		self.ime = ime
	def opis(self):
		print(f"Jaz sem pes z imenom {self.ime}.")
		# return None
		# return
	def vrni_dolzino_imena(self):
		return len(self.ime)

floki = Pes("Floki")
floki.opis()
print(f"Pes {floki.ime} ima ime dolgo {floki.vrni_dolzino_imena()} znakov.")



