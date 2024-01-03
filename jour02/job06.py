class Commande:
    def __init__(self,numero_commande, plats_commandes, statut_commande="en cours"):
        menu_plats = {"pates carbonara": 10,"pizza": 12.50,"salade":8.50, "tiramisu": 7.50,}
        self.__menu_plats = menu_plats
        self.__numero_commande = numero_commande
        self.__plats_commandes = plats_commandes
        self.__statut_commande = statut_commande

    def __ajout_plat__(self, plat):
        if plat in self.__menu_plats:
            self.__plats_commandes[plat] = "en cours"
        else:
            print("Ce plat n'est pas disponible")
        return self.__plats_commandes
    
    def __retirer_plat__(self, plat):
        if plat in self.__plats_commandes:
            self.__plats_commandes.pop(plat)
        else:
            print("Ce plat n'est pas dans la commande")
        return self.__plats_commandes
    
    def __annuler_commande__(self,numero_commande):
        if numero_commande == self.__numero_commande:
            self.__plats_commandes = {}
            self.__statut_commande = "annulée"
            print ("Commande annulée")
            return self.__statut_commande
        
    def __calculer_total__(self):
        total = 0
        for plat in self.__plats_commandes:
            total += self.__menu_plats[plat]
        return total
    
    def __calculer_TVA__(self):
        return self.__calculer_total__() * 0.2
    
    def __terminer_plat__(self, plat):
        if plat in self.__plats_commandes:
            self.__plats_commandes[plat] = "terminé"
        else:
            print("Ce plat n'est pas dans la commande")
        return self.__plats_commandes

    def __terminer_commande__(self):
        self.__statut_commande = "terminée"
        return self.__statut_commande
    

    


commande1 = Commande(1,{"pizza" : "en cours","salade" : "en cours"})
commande2 = Commande(2,{"pates carbonara" : "en cours","salade" : "en cours"})

print (commande1.__ajout_plat__("tiramisu"))
print (commande1.__retirer_plat__("tiramisu"))
print (commande2.__annuler_commande__(2))
print (commande1.__calculer_total__())
print (commande1.__calculer_TVA__())
print (commande1.__terminer_plat__("pizza"))
print (commande1.__terminer_commande__())