class personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def Se_Presenter(self):
        return (f'Je suis {self.prenom} {self.nom}')

personne1 = personne('Doe', 'John').Se_Presenter()
personne2 = personne('Dupond', 'Jean').Se_Presenter()

print (personne1)
print (personne2)