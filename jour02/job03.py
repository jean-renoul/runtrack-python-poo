class livre:
    def __init__(self,titre, auteur, nombre_de_pages,disponible = True):
        self.__titre = titre
        self.__auteur = auteur
        self.__nombre_de_pages = nombre_de_pages
        self.__disponible = disponible

    def __verification__(self):
        return self.__disponible
        
    def __emprunter__(self):
        if self.__verification__() == True:
            self.__disponible = False
            print ("Le livre a été emprunté")
            return self.__disponible
        else:
            print ("Le livre est indisponible")
    
    def __rendre__(self):
        if not self.__verification__():
            self.__disponible = True
            print ("Le livre a été rendu")
            return self.__disponible
        else:
            print ("Le livre est déjà disponible")
    
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

print (exemple.__verification__())
print (exemple.__emprunter__())
print (exemple.__rendre__())