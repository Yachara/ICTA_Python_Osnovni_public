# Napišite funkcion fakulteta, ki uporabnika vpraša naj vnese cifro 
# in izračuna fakulteto te cifre.
#     Fakulteta se izračuna: 3! = 3*2*1 = 6

# Funkcija naj vrne rezultat. 
# Oziroma, če uporabik ni vnesel številke naj funkcija ponovno zahteva od 
# uporabnika vnos cifre.

def fakulteta():
	while True:
		try:
			n = int(input("vnesi n: "))
			break
		except:
			print("Vnešena vrednost ni število!")
	rezultat = 1
	for i in range(1,n+1):
		rezultat = rezultat*i
	return rezultat
# print(fakulteta())

try:
	1/0
except ValueError as e:
	print("dsdsf")
else:
	print("V else-u")
finally:
	print("F")