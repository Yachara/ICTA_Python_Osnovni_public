# Napišite program, ki bo uporabnika uprašal naj vnese
# neko celoštevilsko vrednost. Program naj nato izpiše
# ali je vrednost deljiva z 3 in z 7, ali ne.


vhod = int(input("Vnesi celo število: "))
if vhod%3==0 and vhod%7==0:
	print(f"vhod: {vhod} je deljiv s 3 in 7.")
else:
	print(f"vhod: {vhod} ni deljiv s 3 in 7.")