# Množice (ang. Set)

s = { 
	# <value>
	"medved",
	"zajec",
	"volk",
	"slon",
	"zajec"
}

# s = set({1:2, "a": "vrednost"})
s = set()

print(s)
print(type(s))

# operacije nad množicami
x1 = {1,2,3,4}
x2 = {4,5,6,7}

print(x1 | x2)
# x2 = [4,5,6,7]
print(x1.union(x2))


x1 = {1,2,3,4}
x2 = {4,5}
x3 = {5,6}
x4 = {9,10}
print(x1.union(x2 | x3 | x4))
print(x1.union(x2,x3,x4))

print(x1 & x2)
print(x1.intersection(x2))

print(x1.difference(x2))
print(x1 - x2)

print(x1.symmetric_difference(x2))
print(x1 ^ x2)
print((x1 | x2) - (x1 & x2))

print()
print()

x = {1,2,3,4}
# x.add("string")
# x.remove(4)
# x.discard(5)
# print(x)
# print("First pop:", x.pop())
# print(x)
# print("Secound pop:", x.pop())
# print(x)
# print("Third pop:", x.pop())
# print(x)
x.clear()
print(x)


x = frozenset((1,2,3))
print(x | {1,2,5})
print(x & {1,2,5})
print(x)

x = set(x)
print(x)
