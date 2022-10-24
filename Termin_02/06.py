#  Naloga: Iz sledečega tuple pridobite vrednost cc

our_tuple = ("a", ["bb", "cc"], "d", [("eee"), ["ffff"], "ggg"])

print(our_tuple[1][1])
print(type(our_tuple[1][1]))


# Primer kako lahko spremenimo neko vrednost znotraj lista, ki je znotraj tupla
# ...torej če je nekaj znotraj tupla ne pomeni, da so vse vrednosti "zamrznjene", 
# če je nek objekt znoraj tupla in je "mutable" ga lahko spreminajmo
# print(our_tuple)
# our_tuple[1][0] = "aa"
# our_tuple[1] = [123]
# print(our_tuple)