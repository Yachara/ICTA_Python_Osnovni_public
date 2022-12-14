try:
    x = int(input("Vnesi številko: "))
    rezultat = 10 / x
except ValueError:
    print("To ni številka")
else:
    print("Else statement")
finally:
    print("Finally statement")

print("Nadaljevanje programa")
