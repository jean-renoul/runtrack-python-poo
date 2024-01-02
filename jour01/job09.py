class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def prixTTC(self):
        return round(self.prixHT * (1 + self.TVA/100),2)
    
    def prixTVA(self):
        return round(self.prixTTC() - self.prixHT,2)
    
    def afficher_infos(self):
        return (f"Le produit {self.nom} coûte {self.prixTTC()} € TTC, car son prix hors-taxe est de {self.prixHT} € HT et sa TVA est de {self.TVA} %.")
    
    def modifier_produit(self, nouveau_produit):
        self.nom = nouveau_produit
        return self.nom
    
    def modifier_prixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT
        return self.prixHT
    
    def modifier_TVA(self, nouvelle_TVA):
        self.TVA = nouvelle_TVA
        return self.TVA
    
    def afficher_nom(self):
        return self.nom
    
    def afficher_prixHT(self):
        return self.prixHT
    
    def afficher_TVA(self):
        return self.TVA
    
produit_1 = Produit("dentifrice", 2.50, 20)
produit_2 = Produit("poulet", 10, 33)

print (produit_2.afficher_infos())
print (produit_2.prixTVA())
print (produit_1.modifier_produit("dentifrice à la fraise"))
print (produit_1.modifier_prixHT(3))
print (produit_1.modifier_TVA(10))
print (produit_1.afficher_nom())
print (produit_1.afficher_prixHT())
print (produit_1.afficher_TVA())
print (produit_1.afficher_infos())