# Nadziranje/lovljenje napak

# a = int(input("število: "))

# Try - except - (else - finally)

try:
	a = int(input("število: "))
	a = 1/0
	print("something")
except ZeroDivisionError as err:
	print("Prišlo je do napake pri deljenju z 0!")
except ValueError as err:
	print("Prišlo je do napake prispreminjanju števila iz stringa!")
except Exception as e:
	print("Prišlo je do neke napake, ki ni niti ZeroDevisionError nitit ValueError.")


print("Konec programa.")