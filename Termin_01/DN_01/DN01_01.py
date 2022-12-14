"""
Uporabnika zaprosite naj vnese neko celo število.

To vrednost shranite v spremenljivko z imenom **n** in jo izpišite in izpišite njen tip.

Nato to vrednost pretvorite v float vrednost. Dobljeno float vrednost shranite v spremenljivko **n**. Nato **n** izpišite in izpišite njen tip.
    
Nato spremenljivko n pretvorite v integer vrednost in to shranite v novo spremenljivko **m**. Izpisite m in datatip spremenljivke m.


Primeri:
Input:
5

Output:
<class 'str'>
5

<class 'float'>
5.0

5
<class 'int'>
"""

# rešitevs
n = input("Vnesite celo število: ")

print(type(n))
print(n)
print()


n = float(n)
print(type(n))
print(n)
print()

m = int(n)
print(m)
print(type(m))
