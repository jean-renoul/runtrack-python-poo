class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon
    def changerRayon(self, rayon):
        self.rayon = rayon
    def circonference(self):
        return 2 * 3.14 * self.rayon
    def aire(self):
        return 3.14 * self.rayon**2
    def diametre(self):
        return 2 * self.rayon
    def afficherInfos(self):
        print(f"Rayon : {self.rayon}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")
        print(f"Diamètre : {self.diametre()}")

cercle1 = Cercle(4)
cercle2 = Cercle(7)

cercle1.changerRayon(5)
cercle1.afficherInfos()
print (f"La circonférence du cercle1 est {cercle1.circonference()}")
print (f"L'aire du cercle1 est {cercle1.aire()}")
print (f"Le diamètre du cercle1 est {cercle1.diametre()}")

cercle2.changerRayon(8)
cercle2.afficherInfos()
print (f"La circonférence du cercle2 est {cercle2.circonference()}")
print (f"L'aire du cercle2 est {cercle2.aire()}")
print (f"Le diamètre du cercle2 est {cercle2.diametre()}")