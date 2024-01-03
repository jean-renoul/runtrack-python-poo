class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def get_longueur(self):
        return self.__longueur
    
    def get_largeur(self):
        return self.__largeur
    
    def set_longueur(self, longueur):
        self.__longueur = longueur

    def set_largeur(self, largeur):
        self.__largeur = largeur

exemple = Rectangle(10,5)
print (exemple.get_largeur())
print (exemple.get_longueur())
exemple.set_largeur(20)
exemple.set_longueur(10)
print (exemple.get_largeur())
print (exemple.get_longueur())