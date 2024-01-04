class Ville:
    def __init__(self, nom, nbr_habitants):
        self.__nom = nom
        self.__nbr_habitants = nbr_habitants

    def get_nom(self):
        return self.__nom
    def get_nbr_habitants(self):
        return self.__nbr_habitants
    
    def set_nbr_habitants(self, nbr_habitants):
        self.__nbr_habitants = nbr_habitants
        return self.__nbr_habitants

    
class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        pop = self.__ville.get_nbr_habitants()
        self.__ville.set_nbr_habitants(pop + 1)
        return self.__ville.get_nbr_habitants()

Paris = Ville("Paris", 1000000)
Marseille = Ville("Marseille", 861635)
John = Personne("John", 45, Paris)
Myrtille = Personne("Myrtille", 4, Paris)
Chloé = Personne("Chloé", 18, Marseille)


print (f"Population de la ville de {Paris.get_nom()} : {Paris.get_nbr_habitants()} habitants")
print (f"Population de la ville de {Marseille.get_nom()} : {Marseille.get_nbr_habitants()} habitants")
John.ajouterPopulation()
Myrtille.ajouterPopulation()
print (f"Mise à jour de la population de la ville de {Paris.get_nom()} : {Paris.get_nbr_habitants()} habitants")
Chloé.ajouterPopulation()
print (f"Mise à jour de la population de la ville de {Marseille.get_nom()} : {Marseille.get_nbr_habitants()} habitants")