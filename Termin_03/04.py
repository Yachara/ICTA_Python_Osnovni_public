"""
Napišite program, ki bo pretvoril stopinje Celzija v 
Fahrenheit ali obratno.
Uporabnik naj vnese številko. Nato naj 
vnese v katerih enotah nam je podal vrednost 
(C ali F). Glede na vnešeno črko naj vaš 
program uporabi pravilno formulo za pretvorbo.
T(°F) = T(°C) × 9/5 + 32
T(°C) = (T(°F) - 32) x 5/9
Če uporabnik ni vnesel C ali F naj program 
izpiše Prišlo je do napake.

Primer:
Vnesi vrednost: 12
Vnesi enoto: C
Rešitev:
12 stopinj celzija je enako 53.6 fahrenheit.
"""
# pridobi številko od uporabnika
vrednost = int(input("Vnesi vrednost: "))
# pridobi enoto
enota = input("Vnesi enoto [C/F]: ")
print(f"Uporabnik je vnesel: {vrednost} {enota}")

# poglej ali je enota enaka C -> uporabi formulo za pretvorbo v F
if enota == "C":
    print("Uporabi pretvorbo v Fahrenheit")
    y = vrednost * 9 / 5 + 32
    print(f"{vrednost} {enota} je enako {y} F")
elif enota == "F":
    # poglej ali je enota enaka F -> uporabi pretvorbo v Celzija
    y = (vrednost - 32) * 5 / 9
    print(f"{vrednost} {enota} je enako {y} C")
else:
    # če ni nič od tega, izpiši da je prišlo do napake
    print("Prišlo je do napake")
