"""
Napišite program, ki izpiše prvih 10 sodih števil.
"""
# Neki naj se zgodi 10x
counter = 0
stevilka = 0
while counter < 10:
    if stevilka % 2 == 0:
        print("Sodo št.", stevilka)
        counter += 1
    stevilka += 1
