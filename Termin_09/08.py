# try:
#     f = open("test.txt", "tr")

#     # naredimo operacija
# finally:
#     f.close()

# with open("test.txt") as f:
#     # naredi operacijo
#     pass

# Branje datoteke
# with open("test.txt", "r") as f:
#     file_data = f.read()
#     print(file_data)

# with open("test.txt", "r") as f:
#     prva_vrstica = f.readline()
#     print(prva_vrstica, end="")
#     naslednja_vrstica = f.readline()
#     print(naslednja_vrstica, end="")
#     tretja_vrstica = f.readline()
#     print(tretja_vrstica)

#
# with open("test.txt") as f:
#     # list_of_lines = f.readlines()
#     # print(list_of_lines)
#     for line in f.readlines():
#         line = line.strip()
#         print(line)


# Pisanje v datoteko
# with open("test2.txt", "w") as f:
#     f.write("My first file\n")
#     f.write("Naslednja vrstica")

with open("test2.txt", "a") as f:
    f.write("Add another line\n")
