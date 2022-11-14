# Variable scope
# def funkcija(spr1):
#     spr2 = 10
#     print(f"Spr1: {spr1}")
#     print(f"Spr2: {spr2}")


# funkcija(5)
# print(f"Spr1: {spr1}")
# print(f"Spr2: {spr2}")


# spr1 = 5
# print(f"Spr1: {spr1}")

# if spr1 == 5:
#     spr2 = 10
# print(f"Spr2: {spr2}")
# print()


# def funkcija():
#     spr3 = 200
#     print(f"Spr1: {spr1}")
#     print(f"Spr2: {spr2}")
#     print(f"Spr3: {spr3}")


# funkcija()
# print()
# print(f"Spr1: {spr1}")
# print(f"Spr2: {spr2}")
# print(f"Spr3: {spr3}")


# spr1 = 5
# print(f"Spr1: {spr1}")


# def funkcija():
#     spr1 = 100
#     print(f"Spr1: {spr1}")


# funkcija()
# print(f"Spr1: {spr1}")

# spr1 = 5
# print(f"Spr1: {spr1}")


# def funkcija(spr1):
#     print(f"Spr1: {spr1}")


# funkcija(100)
# print(f"Spr1: {spr1}")


# def funkcija(l):
#     l[0] = 100
#     print(l)


# seznam = [3, 4, 5]
# print(seznam)

# funkcija(seznam)
# print(seznam)

# d = {"a": 5, "b": 6, "c": 7}


# def funkcija(d):
#     d["a"] = 100
#     del d["c"]


# print(d)
# funkcija(d)
# print(d)

# spr1 = 5
# print(f"Spr1: {spr1}")


# def funkcija():
#     global spr1
#     spr1 = 100
#     print(f"Spr1: {spr1}")


# funkcija()
# print(f"Spr1: {spr1}")


def funkcija():
    global spr1
    spr1 = 100
    print(f"Spr1: {spr1}")


funkcija()
print(f"Spr1: {spr1}")
