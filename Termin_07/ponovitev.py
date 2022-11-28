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

floki = Pes("Floki")

print(floki)
print(type(floki))
print(id(floki))

print()
print(floki.opis())



