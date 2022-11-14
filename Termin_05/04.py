# Generators


def moj_range(n):
    print("Start creating my generato")
    while n < 10:
        yield n
        n += 1
    print("Stop generator")


val = moj_range(5)
print(val)
print(type(val))

# x = next(val)
# print(x)

# y = next(val)
# print(y)

# print(next(val))
# print(next(val))
# print(next(val))
# # print(next(val))

# for i in moj_range(5):
#     print(i)
# print("nadaljevanje programa")


def my_range(n, m, step=1):
    while n < m:
        yield n
        n += step  # n = n + step


print("Moj range")
for i in my_range(1, 20, 2):
    print(i)

print("Python range")
for i in range(1, 20, 2):
    print(i)
