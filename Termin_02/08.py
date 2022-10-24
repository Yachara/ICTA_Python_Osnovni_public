# Dictionaries

d = {
	# <ključ> : <vrednost>,
	# <ključ> : <vrednost>,
	# <ključ> : <vrednost>
	"ena": 1,
	"dva":2,
	"macek" : "Silvester",
	"pes" : "Rex",
	"papgaj" : "Kakadudel"
}

print(d)
print(type(d))

print(d["macek"])
print(type(d["macek"]))

print(d["ena"])

# print(d["koza"])

d["koza"] = "Micka"

print(d)
print(type(d))
print(d["koza"])




d["koza"] = "Helga"

print(d)
print(type(d))
print(d["koza"])



del d["koza"]

print(d)
print(type(d))
# print(d["koza"])

print()
print()
print()



d = {
	1: "neakaj",
	2: "neakaj drugega",
	"string" : "c",
	None : 'd',
	2.6864 : "float",
	(1,2,3,"tuple") : "nek tuple",
	1 : "nekaj spet"
}
print(d)
print(d[(1,2,3,"tuple")])
print(d[1])



# d.clear() # izprazni dictionary
# print(d.get(2)) 
# print(d.items())
# print(d.keys())
# print(d.values())
# print(d.pop(2))
print(d.popitem())
print(d)