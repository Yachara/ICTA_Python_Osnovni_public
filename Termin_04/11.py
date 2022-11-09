def hello(name):
	print(f"My name is {name}.")

print("Anže")
print(hello)
funfun = hello

funfun("miha")

fun = [hello, 2,3,"Janez"]
print(fun[0](fun[3]))