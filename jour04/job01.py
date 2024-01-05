class Personne:
    def __init__(self, nom, age=14):
        self.nom = nom
        self.age = age

    def afficherAge(self):
        print(self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age

class Eleve(Personne):
    def __init__(self, nom, age=14):
        Personne.__init__(self, nom, age)

    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print("J'ai", self.age, "ans")

class Professeur(Personne):
    def __init__(self, nom, age, matiere):
        Personne.__init__(self, nom, age)
        self.__matiere = matiere

    def enseigner(self):
        print("Le cours va commencer")

Prof1 = Professeur("Pierre", 32)
Eleve1 = Eleve("Jean")

Eleve1.afficherAge()
Eleve1.modifierAge(30)
Eleve1.afficherAge()
Eleve1.allerEnCours()
Eleve1.bonjour()
Prof1.enseigner()
Prof1.afficherAge()