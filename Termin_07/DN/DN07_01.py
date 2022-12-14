"""
Naloga: 
Napiši razred Zaposlena_oseba, ki ima v sebi shranjene parametre ime, priimek in placa, ki jih prejme ob inicializaciji. 
Vsebuje naj tudi funkcijo razlika_v_placi ki kot parameter prejme objekt tipa Zaposlena_oseba ki predstavlja neko drugo osebo. 
Funkcija naj vrne absolutno razliko med plačama osebe v kateri se funkcija kliče ter pa osebe, ki je bila podana kot parameter.
Ne pozabite na parameter "self". Uporabite ga tam kjer je potrebno.
Primeri:

Input:
    zaposleni = [Zaposlena_oseba("Luka", "Novak", 1500.0),
                 Zaposlena_oseba("Živa", "Groza", 2100.0),
                 Zaposlena_oseba("Anže", "Jaklin", 1436.50),
                 Zaposlena_oseba("Luka", "Bogataj", 1790.0),
                 Zaposlena_oseba("Sara", "Ljubljen", 3600.0)]

    print("Razlika med plačami zaposlenih:")
    for i in range(len(zaposleni)):
        for j in range(i+1, len(zaposleni)):
            ime1 = zaposleni[i].ime
            priimek1 = zaposleni[i].priimek
            razlika = zaposleni[i].razlika_v_placi(zaposleni[j])
            ime2 = zaposleni[j].ime
            priimek2 = zaposleni[j].priimek
            print(f"\t{ime1} {priimek1} <--- {razlika} € ---> {ime2} {priimek2}")

Output:
    Razlika med plačami zaposlenih:
        Luka Novak <--- 600.0 € ---> Živa Groza
        Luka Novak <--- 63.5 € ---> Anže Jaklin
        Luka Novak <--- 290.0 € ---> Luka Bogataj
        Luka Novak <--- 2100.0 € ---> Sara Ljubljen
        Živa Groza <--- 663.5 € ---> Anže Jaklin
        Živa Groza <--- 310.0 € ---> Luka Bogataj
        Živa Groza <--- 1500.0 € ---> Sara Ljubljen
        Anže Jaklin <--- 353.5 € ---> Luka Bogataj
        Anže Jaklin <--- 2163.5 € ---> Sara Ljubljen
        Luka Bogataj <--- 1810.0 € ---> Sara Ljubljen
"""


class Zaposlena_oseba:
    def __init__(self, ime, priimek, placa):
        self.ime = ime
        self.priimek = priimek
        self.placa = placa

    def razlika_v_placi(self, druga_oseba):
        return abs(self.placa - druga_oseba.placa)


zaposleni = [
    Zaposlena_oseba("Luka", "Novak", 1500.0),
    Zaposlena_oseba("Živa", "Groza", 2100.0),
    Zaposlena_oseba("Anže", "Jaklin", 1436.50),
    Zaposlena_oseba("Luka", "Bogataj", 1790.0),
    Zaposlena_oseba("Sara", "Ljubljen", 3600.0),
]

print("Razlika med plačami zaposlenih:")
for i in range(len(zaposleni)):
    for j in range(i + 1, len(zaposleni)):
        ime1 = zaposleni[i].ime
        priimek1 = zaposleni[i].priimek
        razlika = zaposleni[i].razlika_v_placi(zaposleni[j])
        ime2 = zaposleni[j].ime
        priimek2 = zaposleni[j].priimek
        print(f"\t{ime1} {priimek1} <--- {razlika} € ---> {ime2} {priimek2}")

# DN_02
class Krizci_in_krozci:
    def __init__(self):
        self.mreza = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def mark_X(self, row_index, column_index):
        self.mreza[row_index][column_index] = "X"

    def mark_O(self, row_index, column_index):
        self.mreza[row_index][column_index] = "O"

    def check_win(self):
        win_mark = ""
        if (
            self.mreza[0][0] == self.mreza[1][0] == self.mreza[2][0] != " "
        ):  # left column
            win_mark = self.mreza[0][0]
        elif (
            self.mreza[0][1] == self.mreza[1][1] == self.mreza[2][1] != " "
        ):  # middle column
            win_mark = self.mreza[0][1]
        elif (
            self.mreza[0][2] == self.mreza[1][2] == self.mreza[2][2] != " "
        ):  # right column
            win_mark = self.mreza[0][2]
        elif self.mreza[0][0] == self.mreza[0][1] == self.mreza[0][2] != " ":  # top row
            win_mark = self.mreza[0][0]
        elif (
            self.mreza[1][0] == self.mreza[1][1] == self.mreza[1][2] != " "
        ):  # middle row
            win_mark = self.mreza[1][0]
        elif (
            self.mreza[2][0] == self.mreza[2][1] == self.mreza[2][2] != " "
        ):  # bottom row
            win_mark = self.mreza[2][0]
        elif (
            self.mreza[0][0] == self.mreza[1][1] == self.mreza[2][2] != " "
        ):  # diagonal left-top to right-bottom
            win_mark = self.mreza[0][0]
        elif (
            self.mreza[0][2] == self.mreza[1][1] == self.mreza[2][0] != " "
        ):  # diagonal left-bottom to right-top
            win_mark = self.mreza[2][0]

        if win_mark != "":
            print(f"Igralec, ki je označeval z {win_mark}-em je zmagovalec!")

    def reset(self):
        self.mreza = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    def print_current_position(self):
        print(f"-------------")
        print(f"| {self.mreza[0][0]} | {self.mreza[0][1]} | {self.mreza[0][2]} |")
        print(f"-------------")
        print(f"| {self.mreza[1][0]} | {self.mreza[1][1]} | {self.mreza[1][2]} |")
        print(f"-------------")
        print(f"| {self.mreza[2][0]} | {self.mreza[2][1]} | {self.mreza[2][2]} |")
        print(f"-------------")
