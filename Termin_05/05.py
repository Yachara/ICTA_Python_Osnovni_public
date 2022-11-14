# Comprehensions

cela_stevila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# squares = []
# for i in cela_stevila:
#     x = i**2
#     squares.append(x)
# squares = [x**2 for x in cela_stevila]
# print(squares)

# even_squares = [x**2 for x in cela_stevila if x % 2 == 0]
# print(even_squares)

# even_squares = {x**2 for x in cela_stevila if x % 2 == 0}
# print(even_squares)
# print(type(even_squares))

dict_ = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_squared = {f"kljuc_{k}": v**2 for k, v in dict_.items()}
print(dict_squared)
print(type(dict_squared))
