class animal:
    def __init__(self, age=0, prenom=""):
        self.age = age
        self.prenom = prenom

    def vieillir(self):
        self.age += 1
        return self.age
    
    def nommer(self,prenom):
        self.prenom = prenom
        return self.prenom

exemple_animal = animal()
exemple_animal.vieillir()
exemple_animal.vieillir()
print (f"L'âge de l'animal {exemple_animal.age} ans")

exemple_animal.nommer("Luna")
print (f"L'animal se nomme {exemple_animal.prenom}")