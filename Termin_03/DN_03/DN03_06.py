"""
Napišite program, ki od uporabnika zahteva neko celo število.
Program naj nato izračuna fakulteto te številke.

Fakulteta 5:
5! = 5*4*3*2*1 = 120

Primeri:

Input: 4
Output: 24 
"""

# Rešitev
n = int(input("Vnesi št: "))
rezultat = 1

for i in range(1, n + 1):
    rezultat *= i
print(rezultat)
