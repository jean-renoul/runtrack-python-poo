class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationVehicule(self):
        print("Marque =", self.marque)
        print("Modele =", self.modele)
        print("Annee =", self.annee)
        print("Prix =", self.prix)

    def demarrer(self):
        print("Attention, je roule.")

class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.portes = portes

    def informationVehicule(self):
        Vehicule.informationVehicule(self)
        print("Nombre de portes =", self.portes)

    def demarrer(self):
        print("Je suis une voiture et je roule.")   

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = roue

    def informationVehicule(self):
        Vehicule.informationVehicule(self)
        print("Nombre de roues =", self.roue)

    def demarrer(self):
        print("Je suis une moto et je roule.")
        

exemple = Voiture("Mercedes", "Classe A", 2020, 18500)
exemple2 = Moto("Yamaha", "MT-07", 2019, 7000)

exemple.informationVehicule()
exemple2.informationVehicule()
exemple.demarrer()
exemple2.demarrer()