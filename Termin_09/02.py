def delilnik_pozitivnih_st():
    x = input("Vnesi prvo pozitivno število: ")
    x = int(x)
    if x < 0:
        raise ValueError("Vnešena številka mora biti pozitivna")

    y = int(input("Vnesi drugo število: "))
    if y < 0:
        raise ValueError("Vnešena številka mora biutii pozitivna.!!")
    rezultat = x / y
    print(f"{x} / {y} = {rezultat}")


for _ in range(3):
    try:
        delilnik_pozitivnih_st()
    except ZeroDivisionError as exp:
        print("NE SMEŠ DELJITI Z 0!")
        print(exp)
    except Exception as exp:
        print("Splošni exception.")
        print(exp)
