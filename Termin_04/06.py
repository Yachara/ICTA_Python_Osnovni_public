
# Naloga:
# Napišite funkcijo, ki od uporabnika zahteva naj vnese svojo EMŠO število.
# Funkcija naj nato izpiše koliko let je uporabnik star.

# EMŠO ima 14 številk XXXXyyyXXXXXXX. 5.,6.,7. številka predstavljajo letnico
# rojstva (999 -> 1999 leto rojstva).

# neka funkcija
def koliko_sem_star():
	# zahtevaj od uporabnika EMŠO
	emso = input("Vnesi svoj EMŠO: ")
	# Izračunaj letnico rojstva
	letnica_rojstva = int(emso[4:7]) + 1000
	# preveri če je rojen v letu 2000+
	if emso[4] == "0":
		letnica_rojstva += 1000 # identično temu : letnica_rojstva = letnica_rojstva + 1000
	# izračunaj starost
	starost = 2022-letnica_rojstva
	# izpiši starost
	print(f"Star si {starost} let.")

# kliči funkcijo
# koliko_sem_star()

a = ["9","9","8"]
print(type(a),a)
a = "+".join(a)
print(type(a),a)
a = int(a)
print(type(a),a)