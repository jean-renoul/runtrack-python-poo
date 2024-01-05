import random
import time

class Carte:
    def __init__(self, couleur, valeur):
        self.couleur = couleur
        self.valeur = valeur

class Jeu:
    def __init__(self):
        self.paquet = []
        for couleur in ["coeur", "carreau", "pique", "trefle"]:
            for valeur in ["as", "2", "3", "4", "5", "6", "7", "8", "9", "10", "valet", "dame", "roi"]:
                self.paquet.append(Carte(couleur, valeur))

    def melanger(self):
        random.shuffle(self.paquet)

    def tirer(self):
        return self.paquet.pop()
        
    
class Joueur:
    def __init__(self, nom, main=None, force=0):
        self.nom = nom
        self.main = main if main is not None else []
        self.force = force


    def tirer(self, jeu):
        carte = jeu.tirer()
        self.main.append(carte)
        
        if carte.valeur.isdigit():
            self.force += int(carte.valeur)
        elif carte.valeur in ["valet", "dame", "roi"]:
            self.force += 10
        elif carte.valeur == "as":
            if self.nom == "joueur":
                prompt_as = input("Voulez-vous que l'as vaille 1 ou 11 ? ")
                if prompt_as == "1":
                    self.force += 1
                elif prompt_as == "11":
                    self.force += 11
            elif self.nom == "croupier":
                if self.force + 11 > 21:
                    self.force += 1
                else:
                    self.force += 11
        print (f"Carte tirée : {carte.valeur} de {carte.couleur}")
        time.sleep(1)
        return carte.valeur, carte.couleur
    
    

        
class Partie:
    def __init__(self, joueur, croupier):
        self.joueur = joueur
        self.croupier = croupier

    def jouer(self, jeu):
        prompt_joueur = ""
        jeu.melanger()

        joueur.tirer(jeu)
        joueur.tirer(jeu)
        if joueur.force == 21:
            Partie.check_victoire(self)
        
        print(f"Main du {joueur.nom}: {[(c.valeur,"de", c.couleur) for c in joueur.main]} - Force: {joueur.force}")

        croupier.tirer(jeu)
        croupier.tirer(jeu)
        if croupier.force == 21:
            Partie.check_victoire(self)
        
        print(f"Main du {croupier.nom}: {[(c.valeur,"de", c.couleur) for c in croupier.main]} - Force: {croupier.force}")

        while joueur.force < 21 and croupier.force < 21:

            if prompt_joueur != "non":
                prompt_joueur = input("Voulez-vous tirer une carte ? (oui/non) ")
                if prompt_joueur == "oui":
                    joueur.tirer(jeu)                
                    print(f"Main du {joueur.nom}: {[(c.valeur,"de", c.couleur) for c in joueur.main]} - Force: {joueur.force}")
                elif prompt_joueur == "non" and croupier.force >= 17:
                    break
                elif prompt_joueur == "non":
                    pass           
                
            if croupier.force < 17:
                croupier.tirer(jeu)
                print(f"Main du {croupier.nom}: {[(c.valeur,"de", c.couleur) for c in croupier.main]} - Force: {croupier.force}")
            elif prompt_joueur == "non" and croupier.force >= 17:
                break
            elif croupier.force >= 17:
                pass
            

        Partie.check_victoire(self)
                
            

    def check_victoire(self):

        if joueur.force > 21:
            print(f"Le {joueur.nom} a perdu !")
        elif croupier.force > 21:
            print(f"Le {croupier.nom} a perdu !")
        elif joueur.force == 21:
            print(f"Le {joueur.nom} a gagné !")
        elif croupier.force == 21:
            print(f"Le {croupier.nom} a gagné !")
        elif joueur.force > croupier.force:
            print(f"Le {joueur.nom} a gagné !")
        elif croupier.force > joueur.force:
            print(f"Le {croupier.nom} a gagné !")
        elif joueur.force == croupier.force:
            print("Egalité !")


jeu = Jeu()
joueur = Joueur("joueur")
croupier = Joueur("croupier")
partie = Partie(joueur, croupier)

partie.jouer(jeu)