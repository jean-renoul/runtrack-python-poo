class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def perimetre(self):
        return (self.__longueur + self.__largeur) * 2
    
    def surface(self):
        return self.__longueur * self.__largeur
    
    def getLongueur(self):
        return self.__longueur
    
    def getLargeur(self):
        return self.__largeur
    
    def setLongueur(self, longueur):
        self.__longueur = longueur

    def setLargeur(self, largeur):
        self.__largeur = largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.getLongueur() * self.getLargeur()

exemple = Parallelepipede(5, 10, 5)

print(exemple.perimetre())
print(exemple.surface())
print(exemple.volume())
print(exemple.getLongueur())
print(exemple.getLargeur())
exemple.setLongueur(10)
exemple.setLargeur(20)
print(exemple.getLongueur())
print(exemple.getLargeur())

