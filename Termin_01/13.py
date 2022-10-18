# Lists
from re import M


živali = ["pingvin", "medved", "los", "volk"]
# print(živali)
# print(type(živali))

# Lists are orderd
a = ["pingvin", "medved", "los", "volk"]
b = ["los", "medved", "pingvin", "volk"]
# print(a == b)

# Lists can contain arbitrary objects
a = [21.42, "medved", 3, 3, "velk", False, 3 + 4j]
# print(type(a))
# print(a)

# Lists elements can be access by index
a = ["foo", "bar", "baz", "qux", "quux", "corge"]
# print(a[0])
# print(a[1])
# print(a[5])

# print(a[-1])
# print(a[-3])

## Slicing
a = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
# b = a[:5]
# b = a[3:]
# b = a[2:7]
b = a[2:7:2]
print(b)

# Lists can be nested to any depth
x = ["a", ["bb", ["ccc", "ddd"], "ee", "ff"], "g", ["hh", "ii"], "j"]

print(x)
print(x[1])  # ["bb", ["ccc", "ddd"], "ee", "ff"]
print(x[1][1])  # ["ccc", "ddd"]
print(x[1][1][0])  # "ccc"
