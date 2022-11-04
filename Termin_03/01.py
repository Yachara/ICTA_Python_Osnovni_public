# Lists
# l_ = ["string", 12234, 12.3, 12 + 4j]
# print(l_)
# print(type(l_))
# print(l_[-2])

# chess_board = [
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
#     [1, 2, 3, 4, 5, 6, 7, 8],
# ]
# print(chess_board)
# chess_board[0][0] = "trdnjava"
# print(chess_board)

# cela_stevila = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(cela_stevila)
# cela_stevila.append(10)
# print(cela_stevila)
# cela_stevila[-1] = "moj_string"
# print(cela_stevila)

# # TUPLES
# t_ = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(t_)
# print(type(t_))
# print(t_[-1])
# # t_[-1] = "moj_string"
# # print(t_)

# # Dictionary
# d_ = {"a": "moja_spremenljivka", "b": 1234}
# print(d_)
# print(type(d_))
# print(d_["b"])
# d_["b"] = "nova_vrednost"
# print(d_)
# d_["nov_ključ"] = 12.23
# print(d_)

# d_ = {1: "vrednost 1", 2: "vrednost 2", 2: "vrednost 3"}
# print(d_)
# d_[2] = "vrednost 4"
# print(d_)

# d_ = {1000: {"n_prebivalcev": 300_000, "vreme": ""}, 2000: "neki"}

# l_ = [
#     1,
#     2,
#     3,
#     4,
#     5,
#     4,
#     3,
#     4,
#     5,
#     6,
#     5,
# ]
# l_ = list(set(l_))
# print(l_)

# # Range
# l_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = list(range(-5, 10, 2))
# print(x)
# print(type(x))


moj_string = "Danes je lep dan"
print(moj_string[0])
print(moj_string[:5])
# moj_string[-1] = "!"
# "$ 500"
cena = "$ 500"
pretvorba = 0.9
x = int(cena[2:]) * pretvorba
print(x, "€")
