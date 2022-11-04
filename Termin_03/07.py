"""
Uporabnik naj vnese željeno dolžino Fibonaccijevega 
zaporedja. Program naj nato to zaporedje shrani 
v list in ga na koncu izpiše.

Fibonacci sequence
0, 1, 1, 2, 3, 5, 8, 13, 21, 34
"""
dolzina = int(input("Vnesi dolzino fibonacijevega zaporedja: "))
fibonacci = [0, 1]
if dolzina == 0:
    fibonacci = []
elif dolzina == 1:
    fibonacci = [0]
else:
    counter = 0
    while counter < dolzina - 2:
        nova_cifra = fibonacci[-1] + fibonacci[-2]
        print(nova_cifra)
        fibonacci.append(nova_cifra)
        counter += 1
print(fibonacci)
