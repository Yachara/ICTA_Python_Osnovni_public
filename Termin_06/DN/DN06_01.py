"""
Napišite razred Kvader.

Ko ustvarimo novo instanco razreda Kvader, vanj vnesemo dolžino, širino in višino.

Razred naj vsebuje 2 metodi:
* get_volume()          naj vrne volumen kvadra
* get_surface_area()    naj vrne velikost celotne površine

Input:
k1 = Kvader(3, 4, 5)
print(k1.get_volume())
print(k1.get_surface_area())

Outputs:
Volumen:  60
Površina: 94
"""


class Kvader:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_volume(self):
        return self.length * self.width * self.height

    def get_surface_area(self):
        return (
            2 * (self.length * self.height)
            + 2 * (self.length * self.width)
            + 2 * (self.height * self.width)
        )


k1 = Kvader(3, 4, 5)
print("Volumen: ", k1.get_volume())
print("Površina:", k1.get_surface_area())
