# Rešitev
class Gorivo:
    def __init__(self, ime, euro_na_liter):
        self.ime = ime
        self.euro_na_liter = euro_na_liter
        
class Crpalka:
    def __init__(self, goriva):
        self.goriva = goriva
        
    def vsa_goriva(self):
        l = []
        for g in self.goriva:
            l.append(g.ime)
        return l
    
    def najcenejse_gorivo(self):
        name = self.goriva[0].ime
        cheapest = self.goriva[0].euro_na_liter
        for g in self.goriva:
            if g.euro_na_liter < cheapest:
                name = g.ime
        return name
    
    def najdrazje_gorivo(self):
        name = self.goriva[0].ime
        expensive = self.goriva[0].euro_na_liter
        for g in self.goriva:
            if g.euro_na_liter > expensive:
                name = g.ime
        return name
    
    def dodaj_gorivo(self, novo_gorivo):
        for g in self.goriva:
            if g.ime == novo_gorivo.ime:
                print("To gorivo že obstaja")
                return None
        self.goriva.append(novo_gorivo)
            
        
gorivo1 = Gorivo("bencin-7", 3.864)
gorivo2 = Gorivo("dizel", 2.999)
gorivo3 = Gorivo("nafta-3",4.3333)

crpalka = Crpalka([gorivo1, gorivo2, gorivo3])

print("Vsa goriva na črpalki:")
for g in crpalka.vsa_goriva():
    print("*  ", g)
    

print("Najcenejše gorivo: ", crpalka.najcenejse_gorivo())
print("Najdražje gorivo: ", crpalka.najdrazje_gorivo())

gorivo4 = Gorivo("bencin-100",3.101)
gorivo5 = Gorivo("dizel-100",3.432)
gorivo6 = Gorivo("dizel", 3.001)

crpalka.dodaj_gorivo(gorivo4)
crpalka.dodaj_gorivo(gorivo5)
crpalka.dodaj_gorivo(gorivo6)

print("Vsa goriva na črpalki:")
for g in crpalka.vsa_goriva():
    print("*  ", g)
    

print("Najcenejše gorivo: ", crpalka.najcenejse_gorivo())
print("Najdražje gorivo: ", crpalka.najdrazje_gorivo())