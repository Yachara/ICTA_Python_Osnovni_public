# FOR loop
# primes = [2, 3, 5, 7, 11]
# for prime in primes:
#     print(f"{prime} je praštevilo.")
# print("NAADALJEVANJE programa")

# ages = (3, 7, 12)
# for age in ages:
#     print(f"This kid is {age} years old.")
# print("Nadaljevanje programa")

# moj_string = "Danes je lep dan."
# for črka in moj_string:
#     print("Črka: ", črka)
# print("Nadaljevanje programa")

# for i in range(10):
#     print("Korak:", i)
# print("Nadaljevanje programa")

# pets = {"macka": 6, "pes": 12, "krava": 20}
# for pet, years in pets.items():
#     # print(value, type(value))
#     print(f"{pet} je star {years} let.")
# print("Nadaljevanje programa")
# print(pets.items())

# pets = {"macka": 6, "pes": 12, "krava": 20}
# for key in pets:
#     print(key)
#     print(pets[key])

# pets = {"macka": 6, "pes": 12, "krava": 20}
# for value in pets.values():
#     print(value)

moj_string = "Danes je lep dan."
for index, črka in enumerate(moj_string):
    print(f"{črka} na mestu {index}")
    if črka == "a":
        print("a se prvič pojavi na mestu ", index + 1)
