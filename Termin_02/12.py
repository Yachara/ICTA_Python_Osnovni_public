#  Naloga: Iz sledečega lista odstranite vrednost,
# ki se nahaja na indexu 4. Vrednost dodajte v 
# dictionary pod ključ d. Nato iz dictionary 
# pridobite vse vrednosti. Te vrednosti 
# shranite v nov set in novonastali set primerjajte
#  ali je enak podanemu set-u.

our_list = [1,2,3,4,5,6,7]
our_dict = {
    "a": 2,
    "b": 5,
    "c": 8,
    "d": 12,
    "e": 357,
    "f": 12
}
our_set = {357, 12, 12, 8, 5, 2, 2}


# x = our_list[4]
# del our_list[4]
x = our_list.pop(4)
print(x)

our_dict["d"] = x

print(our_dict)

vrednosti = our_dict.values()
vrednosti_set = set(vrednosti)
ali_je_enak = (vrednosti_set == our_set)
print(ali_je_enak)