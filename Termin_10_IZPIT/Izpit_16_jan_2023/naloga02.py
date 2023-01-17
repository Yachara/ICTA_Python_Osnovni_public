# Rešitev
def funkcija02(l):
    new_l = []
    for word in l:
        if ("š" in word) or ("č" in word) or ("ž" in word):
            continue
        new_l.append(word)
    return new_l

l = ["avto", "kočija", "banana", "matematika", "šola", "žolna", "čevljar", "zrezek", "pes"]
print(funkcija02(l))