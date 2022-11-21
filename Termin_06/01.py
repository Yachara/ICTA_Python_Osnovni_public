"""
Napišite funkcijo, ki kot argument 
prejme en string. Funkcija naj 
preveri ali je ta string pangram.
Naj vrne True v primeru , da je 
string pangram, v nasprotnem False.

Pangram je beseda v kateri se 
pojavijo vse črke abecede 
(vzemimo angleško abecedo).
"""


# def is_pangram(word):
#     alphabet = {key: 0 for key in "abcdefghijklmnopqrstuvwxyz"}
#     # print(aplhabet)

#     word = word.lower()
#     for ch in word:
#         if ch in alphabet.keys():
#             alphabet[ch] += 1
#     print(alphabet)

#     for key, value in alphabet.items():
#         if value == 0:
#             return False
#     return True


def is_pangram(word):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    alphabet = sorted(alphabet)

    word = word.lower()
    word = word.replace(" ", "")
    word = word.replace(".", "")
    word = word.replace("!", "")
    word = list(set(word))
    word = sorted(word)
    print(alphabet)
    print(word)

    return word == alphabet


str_ = input("Vnesi stavek: ")  # "The Quick brown fox jumps over the lazy dog."
print("Checking: ", str_)

print(is_pangram(str_))
