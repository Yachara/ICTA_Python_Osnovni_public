# Logične operacije

x = False
y = True

print(not x)  # not obrne vrednost boolean spremenljivke

# OR
# | A     	| B     	| OR   	|
# |-------	|-------	|-------	|
# | False 	| False 	| False 	|
# | False 	| True  	| True  	|
# | True  	| False 	| True  	|
# | True  	| True  	| True  	|
a = False
b = True
print(a or b)

# AND
# | A     	| B     	| AND   	|
# |-------	|-------	|-------	|
# | False 	| False 	| False 	|
# | False 	| True  	| False 	|
# | True  	| False 	| Fasle 	|
# | True  	| True  	| True  	|
a = True
b = True
print(a and b)

# IS
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a == c)
print(a is b)
print(a is c)

# IN
x = "b"
print(x in "moja beseda")
