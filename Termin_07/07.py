# multiple inheritance
class SuperA:
	varA = 10
	def fun(self):
		return 11

class SuperB:
	varB = 20
	def fun(self):
		return 21

class Sub(SuperA,SuperB):
	pass

print(Sub.varA)
print(Sub.varB)
temp = Sub()
print(temp.fun())


