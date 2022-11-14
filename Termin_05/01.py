def odstevalnik(num_1, num_2=10):
    print("Hello")
    i = num_1 - num_2
    j = num_2 - num_1
    return (i, j)


a = int(input("Vnesi prvo stevilko: "))
b = int(input("vNESI DRUGO STEVILKO: "))
k, d = odstevalnik(num_1=a, num_2=b)
print("Razlika = ", k, d)
