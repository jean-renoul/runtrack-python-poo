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

class Cercle(Forme):
    def __init__(self, nom, radius):
        Forme.__init__(self, nom)
        self.radius = radius

    def aire(self):
        return self.radius * self.radius * 3.14
    
rectangle = Rectangle("Rectangle", 5, 10)
cercle = Cercle("Cercle", 5)

print(rectangle.aire())
print(cercle.aire())