class point:
    def __init__(self, x = 2, y = 3):
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        return (f'Coordonnées des points : ({self.x},{self.y})')
    
    def afficherX(self):
        return (f'Coordonnée de x : {self.x}')
    
    def afficherY(self):
        return (f'Coordonnée de y : {self.y}')
    
    def changerX(self):
        self.x = int(input("Nouvelle valeur de x : "))
        return (f'Nouvelle coordonnée de x : {self.x}')
    
    def changerY(self):
        self.y = int(input("Nouvelle valeur de y : "))
        return (f'Nouvelle coordonnée de y : {self.y}')
    
exemple = point()
print(exemple.changerX())
print(exemple.afficherLesPoints())
