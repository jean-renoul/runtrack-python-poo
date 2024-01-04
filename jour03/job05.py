import random

class Personnage:
    def __init__(self, nom=str, vie=int):
        self.__nom = nom
        self.__vie = vie

    def attaquer(self, personnage):
        personnage.__vie -= random.randint(1, 3)
        print (f"Le {self.__nom} attaque le {personnage.__nom}")
        return personnage.__vie
    
class Jeu:
    def __init__(self):
        self.__personnages = []
        self.__niveau = str

    def choisirNiveau(self):
        self.__niveau = input("Choisissez un niveau de difficulté (facile, moyen, difficile) : ")
        return self.__niveau
    
    def lancerJeu(self):
        if self.__niveau == "facile":
            joueur = Personnage("Joueur", 5)        
            monstre = Personnage("Monstre", 3)
        elif self.__niveau == "moyen":
            joueur = Personnage("Joueur", 5)        
            monstre = Personnage("Monstre", 5)
        elif self.__niveau == "difficile":
            joueur = Personnage("Joueur", 5)        
            monstre = Personnage("Monstre", 10)
        self.__personnages.append(joueur)        
        self.__personnages.append(monstre)

    def verifier_vie(self):
        for personnage in self.__personnages:
            if personnage._Personnage__vie <= 0:
                print (f"Le {personnage._Personnage__nom} est mort !")
    
    def afficher_vie(self):
        for personnage in self.__personnages:
            print (f"Le {personnage._Personnage__nom} a {personnage._Personnage__vie} points de vie.")

    def game_loop(self):
        while True:            
            self.afficher_vie()
            self.verifier_vie()
            if self.__personnages[0]._Personnage__vie <= 0 or self.__personnages[1]._Personnage__vie <= 0:
                break
            self.__personnages[0].attaquer(self.__personnages[1])
            self.__personnages[1].attaquer(self.__personnages[0])

partie = Jeu()
partie.choisirNiveau()
partie.lancerJeu()
partie.game_loop()