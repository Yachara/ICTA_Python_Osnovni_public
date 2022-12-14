class MojError(Exception):
    pass


try:
    x = int(input("Vnesi pozitivno št: "))
    if x < 0:
        raise MojError("Številka mota bitii pozitivna.")
except MojError as e:
    print(e)
