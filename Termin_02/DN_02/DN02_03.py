"""
Podana imate dva lista. Seštejte njuja predzadnja elementa.

Primeri:

Input:
[1,2,3,4,5]
[6,7,8,9]
Ouput:
12


Input:
[1,2,3,4]
["a", "b", "c", 10, "d"]
Output:
13


Input:
["1", "2", "3", "4"]
[1,2,3,4]
Output:
6
"""
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9]

l1 = [1, 2, 3, 4]
l2 = ["a", "b", "c", 10, "d"]

l1 = ["1", "2", "3", "4"]
l2 = [1, 2, 3, 4]
print(int(l1[-2]) + int(l2[-2]))
