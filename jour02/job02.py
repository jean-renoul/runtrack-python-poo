class livre:
    def __init__(self,titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
    
    def __get_titre__(self):
        return self.__titre
    
    def __get_auteur__(self):
        return self.__auteur
    
    def __get_nombre_de_pages__(self):
        return self.__nombre_de_pages
    
    def __set_titre__(self, titre):
        self.__titre = titre

    def __set_auteur__(self, auteur):
        self.__auteur = auteur

    def __set_nombre_de_pages__(self, nombre_de_pages):
        if nombre_de_pages > 0 and nombre_de_pages == int:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Nombre de pages incorrect")

exemple = livre("Le seigneur des anneaux", "J.R.R. Tolkien", 1000)
print (exemple.__get_titre__())
print (exemple.__get_auteur__())
print (exemple.__get_nombre_de_pages__())
exemple.__set_titre__("Le seigneur des anneaux 2")
exemple.__set_auteur__("Cristiano Ronaldo")
exemple.__set_nombre_de_pages__(-1)
print (exemple.__get_nombre_de_pages__())
print (exemple.__get_titre__())
print (exemple.__get_auteur__())