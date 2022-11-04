"""
Napišite program, ki bo uporabnika uprašal naj 
vnese neko celoštevilsko vrednost. Program naj 
nato izpiše ali je vrednost deljiva z 3 ali ne.
"""
# Pridobi številko od uporabnika
x = int(input("Vnesi celo število: "))
print("X vrednost, ", x)
# Prevri ali je deljivo s 3
print("x%3 = ", x % 3)
if x % 3 == 0:
    print("Število je deljivo s 3")
else:
    print("Število ni deljivo s 3")
