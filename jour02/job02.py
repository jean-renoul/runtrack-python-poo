class livre:
    def __init__(self,titre, auteur, nombre_de_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
    
    def get_titre(self):
        return self.__titre
    
    def get_auteur(self):
        return self.__auteur
    
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages
    
    def set_titre(self, titre):
        self.__titre = titre

    def set_auteur(self, auteur):
        self.__auteur = auteur

    def set_nombre_de_pages(self, nombre_de_pages):
        if nombre_de_pages > 0 and nombre_de_pages == int:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Nombre de pages incorrect")

exemple = livre("Le seigneur des anneaux", "J.R.R. Tolkien", 1000)
print (exemple.get_titre())
print (exemple.get_auteur())
print (exemple.get_nombre_de_pages())
exemple.set_titre("Le seigneur des anneaux 2")
exemple.set_auteur("Cristiano Ronaldo")
exemple.set_nombre_de_pages(-1)
print (exemple.get_nombre_de_pages())
print (exemple.get_titre())
print (exemple.get_auteur())