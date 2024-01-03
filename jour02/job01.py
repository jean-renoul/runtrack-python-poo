class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
    
    def __get_longueur__(self):
        return self.__longueur
    
    def __get_largeur__(self):
        return self.__largeur
    
    def __set_longueur__(self, longueur):
        self.__longueur = longueur

    def __set_largeur__(self, largeur):
        self.__largeur = largeur

exemple = Rectangle(10,5)
print (exemple.__get_largeur__())
print (exemple.__get_longueur__())
exemple.__set_largeur__(20)
exemple.__set_longueur__(10)
print (exemple.__get_largeur__())
print (exemple.__get_longueur__())