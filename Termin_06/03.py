# https://collabedit.com/87njg
"""
Napišite funkcijo, kjer lahko igramo vislice.

Funkcija vislice() naj ima 2 parametra. Prvi je besedo 
katero se ugiba in drugi število možnih ugibov. 
Če števila ugibov ne podamo naj bo default vrednost 10.

Uporabnika konstantno sprašujte naj vnese črko. 
Nato izpišite iskano besedo. Črke katere je uporabnik 
uganil izpišite normalno, črke katere še ni 
uganil pa nadomestite z _.

Dodatno zraven prikazujte katere vse črke je 
uporabnik že preizkusil.

Če uporabnik besedo uspešno ugani v danih 
poizkusih naj funkcija vrne vrednost True. 
V nasprotnem primeru naj vrne vrednost False.

Primeri:

Input:
vislice("jabolko")

Output:
Guesses so far []. 
What is your guess? a
_ a_ _ _ _ _ 

Guesses so far ['a']. 
What is your guess? e
_ a_ _ _ _ _ 

Guesses so far ['a', 'e']. 
What is your guess? o
_ a_ o_ _ o

Guesses so far ['a', 'e', 'o']. 
What is your guess? p
_ a_ o_ _ o

Guesses so far ['a', 'e', 'o', 'p']. 
What is your guess? r
_ a_ o_ _ o

Guesses so far ['a', 'e', 'o', 'p', 'r']. 
What is your guess? l
_ a_ ol_ o

Guesses so far ['a', 'e', 'o', 'p', 'r', 'l']. 
What is your guess? k
_ a_ olko

Guesses so far ['a', 'e', 'o', 'p', 'r', 'l', 'k']. 
What is your guess? j
ja_ olko

Guesses so far ['a', 'e', 'o', 'p', 'r', 'l', 'k', 'j']. 
What is your guess? b
jabolko
KONEC
True
"""


def vislice(beseda, n=10):
    correct_guesses = []
    all_guesses = []

    try_ = 0
    while try_ < n:
        # print vse ugibe
        print(f"Guesses so far: {all_guesses}")

        # zahtevaj input
        guess = input("Vnesi črko: ")
        all_guesses.append(guess)

        # test, če se črka nahaja v besedi
        if guess in beseda:
            correct_guesses.append(guess)

        # print beseda _ _ _ _ _
        beseda_print = ""
        for ch in beseda:
            if ch in correct_guesses:
                beseda_print += ch
            else:
                beseda_print += "_ "
        print(beseda_print)

        # test ali je igralec zmagal
        if len(set(correct_guesses)) == len(set(beseda)):
            print("KONEC")
            return True

        try_ += 1
    return False


print(vislice("jabolko"))
