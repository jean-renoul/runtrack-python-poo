class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    def get_info(self):
        return self.__titre, self.__description, self.__statut
    
    def set_statut(self, statut):
        self.__statut = statut
        return self.__statut


class ListeDeTaches:
    def __init__(self, taches):
        self.__taches = taches

    def ajouterTache(self, tache):
        self.__taches.append(tache)
        
    def supprimerTache(self, tache):
        self.__taches.remove(tache)

    def marquerCommeFinie(self, tache):
        tache.set_statut("finie")

    def afficherListe(self):
        for tache in self.__taches:
            print(tache.get_info())

    def filterListe(self, statut):
        for tache in self.__taches:
            if tache.get_info()[2] == statut:
                print(tache.get_info())
    
tondre_pelouse = Tache("Tondre la pelouse", "Tondre la pelouse du jardin")
reparer_frigo = Tache("Réparer le frigo", "Réparer le frigo qui ne fait plus de froid")
laver_voiture = Tache("Laver la voiture", "Laver la voiture qui est sale")
appeler_mamie = Tache("Appeler mamie", "Appeler mamie pour prendre des nouvelles")

liste_de_taches = ListeDeTaches([])

liste_de_taches.ajouterTache(tondre_pelouse)
liste_de_taches.ajouterTache(reparer_frigo)
liste_de_taches.ajouterTache(laver_voiture)
liste_de_taches.ajouterTache(appeler_mamie)
liste_de_taches.afficherListe()
liste_de_taches.supprimerTache(reparer_frigo)
liste_de_taches.marquerCommeFinie(tondre_pelouse)
liste_de_taches.filterListe("à faire")