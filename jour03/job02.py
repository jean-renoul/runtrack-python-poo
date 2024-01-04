class CompteBancaire:
    def __init__(self, numero, nom, prenom, solde,decouvert):
        self.__numero = numero
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print (f"Le numéro de compte de {self.__prenom} {self.__nom} est {self.__numero}")

    def afficherSolde(self):
        print (f"Le solde du compte de {self.__prenom} {self.__nom} est de {self.__solde} euros")

    

    def versement(self, montant):
        if isinstance(montant, int):
            self.__solde += montant
            return self.__solde
        else:
            print ("Le montant doit être un nombre entier")
    
    def retrait(self, montant):
        if isinstance(montant, int):
            if self.__solde >= montant or self.__decouvert == True:
                self.__solde -= int(montant)
                if self.__solde < 0:
                    self.agios()
                    return self.__solde
                else:
                    return self.__solde
            else:
                return "Vous n'avez pas assez d'argent sur votre compte"
        else:
            print ("Le montant doit être un nombre entier")

    def agios(self):
        if self.__solde < 0:
            self.__solde += self.__solde * 0.10
            return self.__solde
        
    def virement(self,référence,destinataire,montant):
        if référence == f"{self.__numero},{self.__nom},{self.__prenom}":
            if self.__solde >= montant or self.__decouvert == True:                
                self.retrait(montant)
                destinataire.versement(montant)
                print (f"Le virement de {montant} euros a bien été effectué")
            else:
                print ("Vous n'avez pas assez d'argent sur votre compte")
        else:
            print ("Référence incorrecte")
        return self.__solde, destinataire.__solde
            
            
                

jean = CompteBancaire(123456789, "Renoul", "Jean", 1000, True)
anais = CompteBancaire(987654321, "Bourgeois", "Anaïs", -100, True)

jean.afficher()
jean.afficherSolde()
print (jean.versement(100))
print (jean.retrait(100))
print (jean.virement("123456789,Renoul,Jean",anais,2000))