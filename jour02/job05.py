class Voiture:
    def __init__(self, marque, modele, année, kilometrage, en_marche=False, reservoir=50):
        self.__marque = marque
        self.__modele = modele
        self.__année = année
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    def __get_marque__(self):
        return self.__marque
    def __get_modele__(self):
        return self.__modele
    def __get_année__(self):
        return self.__année
    def __get_kilometrage__(self):
        return self.__kilometrage
    def __get_en_marche__(self):
        return self.__en_marche
    
    def __set_marque__(self, marque):
        self.__marque = marque
        return self.__marque
    def __set_modele__(self, modele):
        self.__modele = modele
        return self.__modele
    def __set_année__(self, année):
        self.__année = année
        return self.__année
    def __set_kilometrage__(self, kilometrage):
        self.__kilometrage = kilometrage
        return self.__kilometrage
    def __set_en_marche__(self, en_marche):
        self.__en_marche = en_marche
        return self.__en_marche

    def __demarrer__(self):
        if self.__en_marche == True:
            print("La voiture est déjà démarrée")
        else:
            if self.__verifier_plein__() > 5:
                self.__en_marche = True
                print("La voiture démarre")
            else:
                print ("La voiture n'a pas assez d'essence pour démarrer")
    
    def __arreter__(self):
        if self.__en_marche == False:
            print("La voiture est déjà arrêtée")
        else:
            self.__en_marche = False
            print("La voiture s'arrête")

    def __verifier_plein__(self):
        return self.__reservoir
    
voiture = Voiture("Renault", "Clio", 2005, 100000)
print(voiture.__get_année__())
print(voiture.__get_en_marche__())
print(voiture.__get_kilometrage__())
print(voiture.__get_marque__())
print(voiture.__get_modele__())
print(voiture.__set_année__(2006))
print(voiture.__set_en_marche__(False))
print(voiture.__set_kilometrage__(100001))
print(voiture.__set_marque__("Audi"))
print(voiture.__set_modele__("TT"))
print(voiture.__verifier_plein__())
voiture.__demarrer__()
voiture.__arreter__()