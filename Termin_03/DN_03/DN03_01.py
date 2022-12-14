"""
Izpišite srednje 3 črke podanega string-a.

Za določanje dolžine stringa lahko uporabite funkcijo len(string)

len("World") je enako 5.

Primeri:

Input: World
Output: orl

Input: Python Programming Language
Output: amm

Input: 1234abc
Output: 34a
"""

# Rešitev
str_ = "World"
# str_ = "Python Programming Language"
# str_ = "1234abc"
print(len(str_))

middleIndex = int(len(str_) / 2)
print(str_)
middleThree = str_[middleIndex - 1 : middleIndex + 2]
print(middleThree)
