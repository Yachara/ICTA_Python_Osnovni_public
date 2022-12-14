def delilnik():
    x = input("Vnesi prvo število: ")
    x = int(x)
    y = int(input("Vnesi drugo število: "))
    rezultat = x / y
    print(f"{x} / {y} = {rezultat}")


for _ in range(3):
    try:
        delilnik()
    except ZeroDivisionError as exp:
        print("NE SMEŠ DELJITI Z 0!")
        print(exp)
    except Exception as exp:
        print("Splošni exception.")
        print(exp)
