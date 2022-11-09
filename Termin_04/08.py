
# Naloga:

# Napiši funkcijo, ki sprejme 3 argumente (integer števila).

# Funkcija naj izpiše kateri ima največjo vrednost in koliko je ta vrednost.

def fun(a,b,c):
	# print(max([a,b,c]))
	if a>=b and a>=c:
		print("Največji je a:",a)
	elif b>=a and b>=c:
		print("Največji je b:",b)
	else:
		print("Največji je c:",c)

fun(1,3,3)