"""
Napišite program, ki preveri ali je neka beseda palindrom.
Palindrom je beseda, ki se bere enako naprej in nazaj. (taco cat  - palindrom, madam - palindrom, ...)

Primeri:

Input: taco cat
Output: Beseda je palindrom

Input: madam
Output: beseda je palindrom

Input: konjederec
Output: beseda ni palindrom
"""

# Rešitev
beseda = "taco cat"
# beseda = "madam"
# beseda = "konjederec"

beseda = beseda.replace(" ", "")
if beseda == beseda[::-1]:
    print("Beseda je palindrom")
else:
    print("Beseda ni palindrom")
