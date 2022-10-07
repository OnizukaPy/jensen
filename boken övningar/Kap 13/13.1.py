class Bok:

    def __init__(self, titel, författare, sidantal, pris):
        self.titel = titel
        self.författare = författare
        self.sidantal = sidantal
        self.pris = pris

    def skriva_info(self):
        
        print(f"\nBoken titel är: {self.titel} och författaren är {self.författare}. Boken har {self.sidantal} sidor coh priset är {self.pris} kr")
    

bok1 = Bok("Python från början", "Jan Skansholm", 295, 500)
bok2 = Bok("Du går inte ensam", "Mari Jungstedt", 150, 110)

bok1.skriva_info()
bok2.skriva_info()