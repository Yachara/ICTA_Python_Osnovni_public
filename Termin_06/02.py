"""
Napišite funkcijo, ki kot argument prejme string 
besed, ki so med seboj povezane z -.

Funkcija naj vrne string, ki je 
sestavljen iz teh besed, povezanih 
med seboj z -, razvrščenih po abecedi.

Primeri:

Input:
Before sort:  brown-orange-red-gray-yellow

Output:
After sort:  brown-gray-orange-red-yellow
"""


def my_sort(str_):
    l_ = str_.split("-")
    l_ = sorted(l_)

    final_word = ""
    for word in l_:
        final_word += word
        final_word += "-"
    return final_word[:-1]


word = "brown-orange-red-gray-yellow"
print("Before sort:", word)
word = my_sort(word)
print("After sort: ", word)
