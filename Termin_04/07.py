def fun(stevilo_min, stevilo_max,a):
	# zahtevaj od uporabnika stevilo v nekem rangu
	if stevilo_max < stevilo_min:
		print("Napaka v programu! Max ni večje ali enak minimumu")
		return
	x = float(input(f"Vnesi število med {stevilo_min} in {stevilo_max}: "))
	x = 3*x + 7
	print(f"Vnesel si {x}")

fun(4,a = 7,stevilo_max=14)
fun(4,7)
fun(4,2)
fun(1,13)
fun(0,6)
