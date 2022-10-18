# Uporabnika vprašajte za 3
# celoštevilske vrednosti in
# jih izpišite s
# pomočjo print() in type().
# V eni vrstici preverite
# ali je druga vrednost
# enaka prvi in ali je
#  tretja vrednost manjša ali enaka prvi.
a = int(input("1: "))
b = int(input("2: "))
c = int(input("3: "))

print(f"Tip: {type(a)}, Vrednost: {a}")
print(f"Tip: {type(b)}, Vrednost: {b}")
print(f"Tip: {type(c)}, Vrednost: {c}")

print(b == a and c <= a)
