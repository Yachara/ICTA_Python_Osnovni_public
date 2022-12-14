"""
Napišite funkcijo, ki kot parameter x premje
neko celo število. Funkcija naj izpiše 
zadnjih x vrstic v datoteki naloga2.txt.

*naloga2.txt2*
line 1
line 2
line 3
line 4
...
INPUT:
funkcija(3)

OUTPUT:
line 7
line 8
line 9
"""


def funkcija(n):
    with open("naloga2.txt", "r") as f:
        data = f.readlines()
        for line in data[-n:]:
            print(line, end="")


funkcija(3)
