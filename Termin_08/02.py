# Naloga

# Ustvarite razred `Polica`.
# Vsaka instanca razreda naj ima:
# 	knjige -> list naslovov knjig, ki se nahajajo na polici
# 	max_knjig -> integer vrednost, ki pove koliko knjig, gre maximalno na polico
# Ko ustvarimo instanco razreda vanj posredujemo številko maximalnih knjig na polici.
# Ko ustvarimo instanco razreda vanj posredujemo lahko tudi list naslovov knjig, 
# ki se že nahajajo na polici. Če takega seznama ne posredujemo naj ima polica 
# prazen seznam.
# Razred naj ima metodo `kaj_je_na_polici`, ki naj vrne list naslovov knjig
# Razred naj ima metodo `dodaj_knjigo`, ki kot argument prejme string naslova knjige.
# To knjigo naj doda v list naslovov knjig (self.knjige), če s tem ne presežemo 
# maximalno število knjig. Če bi presegli to število knjige ne dodamo.

# Razred naj ima metodo `uredi_knjige`, ki kot argument **ascending** prejme
# boolean vrednost, ki nam pove ali naj bodo knjige urejene (glede na prvo črko) 
# v A->Z (vrednost True) oziroma Z->A (vrednost False). 
# Če ta vrednost ni bila posredovana naj bo default vrstni red A->Z. 
# Metoda naj uredi list naslovov knjig in tega nato vrne

class Polica:
	def __init__(self,max_knjig,knjige_ze_na_polici=[]):
		self.knjige = knjige_ze_na_polici # list
		self.max_knjig = max_knjig # int
	def kaj_je_na_polici(self):
		return self.knjige
	def dodaj_knjigo(self,nova_knjiga):
		# nova_knjiga je tipa string
		if len(self.knjige) < self.max_knjig:
			self.knjige.append(nova_knjiga)
	def uredi_knjige(self,ascending=True):
		# "ascending" je boolean vrednost (True/False)
		# 		True --> A-Z
		# 		False --> Z-A
		
		# urejene_knjige_po_abecedi = sorted(self.knjige,reverse= not ascending)
		if ascending:
			urejene_knjige_po_abecedi = sorted(self.knjige)
		else:
			urejene_knjige_po_abecedi = sorted(self.knjige,reverse=True)
		self.knjige = urejene_knjige_po_abecedi
		return self.knjige
	

polica = Polica(7, ["The Witcher", "Dune", "Harry Potter", "Hamlet", "Krautov Strojniški Priročnik", "SSKJ"])
print(polica.kaj_je_na_polici())
# ==> ['The Witcher', 'Dune', 'Harry Potter', 'Hamlet', 'Krautov Strojniški Priročnik', 'SSKJ']

print(polica.uredi_knjige())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'Krautov Strojniški Priročnik', 'SSKJ', 'The Witcher']

polica.dodaj_knjigo("Romeo in Julija")
print(polica.kaj_je_na_polici())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'Krautov Strojniški Priročnik', 'SSKJ', 'The Witcher', 'Romeo in Julija']

polica.dodaj_knjigo("Game of Thrones")
print(polica.kaj_je_na_polici())
# ==> ['Dune', 'Hamlet', 'Harry Potter', 'Krautov Strojniški Priročnik', 'SSKJ', 'The Witcher', 'Romeo in Julija']

print(polica.uredi_knjige(False))
# ==> ['The Witcher', 'SSKJ', 'Romeo in Julija', 'Krautov Strojniški Priročnik', 'Harry Potter', 'Hamlet', 'Dune']

# polica.shrani_knjige()