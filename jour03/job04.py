class Joueur:
    def __init__(self,nom,numero,position,nb_but,nb_passe_de,nb_cartons_jaunes,nb_cartons_rouges):
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_but = nb_but
        self.__nb_passe_de = nb_passe_de
        self.__nb_cartons_jaunes = nb_cartons_jaunes
        self.__nb_cartons_rouges = nb_cartons_rouges

    def set_nom(self,nom):
        self.__nom = nom
        return self.__nom
    def set_numero(self,numero):
        self.__numero = numero
        return self.__numero
    def set_position(self,position):
        self.__position = position
        return self.__position
    def set_nb_but(self,nb_but):
        self.__nb_but = nb_but
        return self.__nb_but
    def set_nb_passe_de(self,nb_passe_de):
        self.__nb_passe_de = nb_passe_de
        return self.__nb_passe_de
    def set_nb_cartons_jaunes(self,nb_cartons_jaunes):
        self.__nb_cartons_jaunes = nb_cartons_jaunes
        return self.__nb_cartons_jaunes
    def set_nb_cartons_rouges(self,nb_cartons_rouges):
        self.__nb_cartons_rouges = nb_cartons_rouges
        return self.__nb_cartons_rouges

    def marquerUnBut(self):
        self.__nb_but += 1
    def effectuerUnePasseDecisive(self):
        self.__nb_passe_de += 1
    def recevoirUnCartonJaune(self):
        self.__nb_cartons_jaunes += 1
    def recevoirUnCartonRouge(self):
        self.__nb_cartons_rouges += 1
    
    def afficherStatistiques(self):
        print (f"Le joueur {self.__nom}, numéro {self.__numero}, {self.__position} a marqué {self.__nb_but} buts, effectué {self.__nb_passe_de} passes décisives, reçu {self.__nb_cartons_jaunes} cartons jaunes et reçu {self.__nb_cartons_rouges} cartons rouges")
        return self.__nb_but, self.__nb_passe_de, self.__nb_cartons_jaunes, self.__nb_cartons_rouges
    
class Equipe:
    def __init__(self,nom,joueurs=None):
        self.__nom = nom
        self.__joueurs = joueurs if joueurs is not None else []

    def ajouterJoueur(self,joueur):
        self.__joueurs.append(joueur)

    def afficherStatistiquesJoueurs(self):
        for joueur in self.__joueurs:
            print (joueur.afficherStatistiques())

    def mettreAJourStatistiquesJoueur(self,joueur,nom,numero,position,nb_but,nb_passe_de,nb_cartons_jaunes,nb_cartons_rouges):
        joueur.set_nom(nom)
        joueur.set_numero(numero)
        joueur.set_position(position)
        joueur.set_nb_but(nb_but)
        joueur.set_nb_passe_de(nb_passe_de)
        joueur.set_nb_cartons_jaunes(nb_cartons_jaunes)
        joueur.set_nb_cartons_rouges(nb_cartons_rouges)
        return joueur.afficherStatistiques()
        
    
Messi = Joueur("Messi",10,"Milieu de terrain",0,0,0,0)
Mbappe = Joueur("Mbappé",7,"Attaquant",0,0,0,0)
Pallois = Joueur("Pallois",4,"Défenseur",0,0,0,0)

Mitroglou = Joueur("Mitroglou",9,"Attaquant",0,0,0,0)
Maguire = Joueur("Maguire",5,"Défenseur",0,0,0,0)
Mctominay = Joueur("Mctominay",39,"Milieu de terrain",0,0,0,0)

FC_Nantes = Equipe("Fc Nantes")
Stade_Rennais = Equipe("Stade Rennais")

FC_Nantes.ajouterJoueur(Messi)
FC_Nantes.ajouterJoueur(Mbappe)
FC_Nantes.ajouterJoueur(Pallois)
Messi.afficherStatistiques()

Stade_Rennais.ajouterJoueur(Mitroglou)
Stade_Rennais.ajouterJoueur(Maguire)
Stade_Rennais.ajouterJoueur(Mctominay)


Messi.marquerUnBut()
Messi.effectuerUnePasseDecisive()
Mbappe.marquerUnBut()
Maguire.recevoirUnCartonRouge()
Pallois.recevoirUnCartonJaune()
Pallois.marquerUnBut()
Messi.effectuerUnePasseDecisive()
Mbappe.marquerUnBut()
Messi.effectuerUnePasseDecisive()
Mitroglou.recevoirUnCartonJaune()
Pallois.marquerUnBut()
Messi.effectuerUnePasseDecisive()

Stade_Rennais.afficherStatistiquesJoueurs()
FC_Nantes.afficherStatistiquesJoueurs()
FC_Nantes.mettreAJourStatistiquesJoueur(Messi,"Messi",39,"Attaquant",420,0,0,0)