#  Naloga: Iz sledečega dictionary
#  pridobite vrednost fff.

d = {
    "a": "a",
    "b": "b",
    "c": {
        1: 11,
        2: 22,
        3: 33,
        4: {
            5: "ccc",
            6: "ddd",
            "7": "fff"
        }
    }
}

print(d.get("c").get(4).get("7"))
print(d["c"][4]["7"])
