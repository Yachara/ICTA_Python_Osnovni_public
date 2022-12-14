"""
Podana imaste dva stringa. Iz njih ustvarite nov string tako, da uporabite prvi dve črk prvega stringa, nato celoten drugi string in na koncu preostanek prvega stringa.

Primeri:

Input:
Marec
April

Output:
MaAprilrec


Input:
Hello
World

Output:
HeWorldllo
"""
str1 = "Marec"
str2 = "April"

str1 = "Hello"
str2 = "World"

new_str = str1[:2] + str2 + str1[2:]
print(new_str)
