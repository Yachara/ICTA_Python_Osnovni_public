import inspect

# več nivojev dedovanja


class Level0:
	var = 9
	def fun(self):
		return 0

class Level1(Level0):
	var = 100
	def fun(self):
		return 101


class Level2(Level1):
	pass

object_  = Level2()
print(object_.var,object_.fun())




print(type(object_))
print(isinstance(object_,Level0))
print(isinstance(object_,Level1))
print(isinstance(object_,Level2))



print(inspect.getmro(Level2))