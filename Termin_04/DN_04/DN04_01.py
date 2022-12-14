"""
Naloga: 
Ustvarite funkcijo, ki prejme list cen v $ in valuto v katero naj spremeni cene.

Funkcija naj odstrani $ in nepotrebne presledke in naj na koncu cene doda podano valuto (ni potrebno računati pravilen menjalni tečaj).

Posodobljene cene naj funkcija vrne.

Primeri:

Input:
prices = ["$53", "$  120", "$ 1222", "$$342", " $ 91", " $ 51", "39$"]
funkcija(prices, "€")

Output:
['53€', '120€', '1222€', '342€', '91€', '51€', '39€']
"""
prices = ["$53", "$  120", "$ 1222", "$$342", " $ 91", " $ 51", "39$"]


def funkcija(l, valuta):
    new_prices = []
    for price in l:
        new_price = ""
        for ch in price:
            if ch == " " or ch == "$":
                pass
            else:
                new_price += ch
        new_price += valuta
        new_prices.append(new_price)
    return new_prices


funkcija(prices, "€")
