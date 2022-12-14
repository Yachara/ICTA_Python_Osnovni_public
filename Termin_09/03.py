"""
Napišite funkcijo is_palindrom, ki od uporabnika 
zahteva naj vnese besedo. Funkcija naj vrne True, 
če je beseda palindrom, v nasprotnem primeru False. 
Palindrom je beseda, ki se prebere isto od leve 
proti desni in od desne proti levi.
Če uporabnik vnese samo številke naj 
funkcija rais-a ValueError.

Program naj 3x zažene funkcijo. V kolikor pride do 
ValueError naj se izpiše sporočilo in izvajanje 
programa nadaljuje.

OUTPUT:
Vnesi besedo: Ananas
The word is NOT palindrom.
Vnesi besedo: 1234
Vnešene so bile samo številke.
Vnesi besedo: racecar
The word is PALINDROM
"""
def is_palindrom():
    beseda = input("Vnesi besedo: ")
    if beseda.isnumeric():
        raise ValueError
    beseda_rev = reversed(beseda)
    if list(beseda) == list(beseda_rev):
        return True
    else:   
        return False

for i in range(3):
   try:
        if is_palindrom():
            print("Beseda JE palindrom")
        else:
            print("Beseda ni palindrom")
    except ValueError as e:
        print("Vnesli smo samo številke")
    
    


