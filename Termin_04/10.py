# Naloga:
# Napišite funkcijo, ki sprejme nabor podatkov v obliki dictionary
# in vrne največjo vrednost vsakega ključa.

def funkcija(podatki):
	najvecje_vrednosti = []
	for key in podatki.values():
		najvecje_vrednosti.append(max(podatki[key]))
	return najvecje_vrednosti

# Input:
data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}

print(funkcija(data))

# Output:
[43033, 50768369805]

print(type(funkcija))