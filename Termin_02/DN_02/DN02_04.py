"""
Iz sledečih dictionary izpišite vrednost "Python"

Primeri:

Input:
{1: 1,
 2: 10,
 3: 100,
 4: "Python",
 5: 5}
Output:
Python


Input:
d = {1: 1,
    2: 10,
    3: {1: 1,
        2: 2,
        3: {
            1: 1,
            2: 2,
            3: 3,
            4: 5,
            5: "Python"
        }
    }}
Output:
Python


Input:
{1: 1,
    2: 10,
    3: {1: 1,
        2: 2,
        3: {
            1: 1,
            2: 2,
        },
    4: [1,2,3,5,{1:1, 2:"Python"}]
    }}
Output:
Python
"""
d = {1: 1, 2: 10, 3: 100, 4: "Python", 5: 5}
print(d[4])


d = {1: 1, 2: 10, 3: {1: 1, 2: 2, 3: {1: 1, 2: 2, 3: 3, 4: 5, 5: "Python"}}}
print(d[3][3][5])


d = {
    "a": 1,
    "b": 10,
    "c": {
        1: 1,
        2: 2,
        "x": {
            1: 1,
            2: 2,
        },
        "d": [1, 2, 3, 5, {1: 1, 2: "Python"}],
    },
}
print(d["c"]["d"][4][2])
