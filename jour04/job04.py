class Forme:
    def __init__(self, nom):
        self.nom = nom

    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, nom, hauteur, largeur):
        Forme.__init__(self, nom)
        self.hauteur = hauteur
        self.largeur = largeur
    
    def aire(self):
        return self.hauteur * self.largeur
    

exemple = Forme("Forme")
exemple2 = Rectangle("Rectangle",5, 10)

print (exemple.aire())
print (exemple2.aire())