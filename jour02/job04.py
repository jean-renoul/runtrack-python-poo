class Student:
    def __init__(self,nom,prenom,numero_etudiant,credits=0,level=""):        
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__credits = credits
        self.__level = level
        self.__level = self.__studentEval__()
        
    
    def __add_credits__(self,ajout_credits):
        if ajout_credits > 0:
            self.__credits += ajout_credits
            self.__level = self.__studentEval__()

    def __get_credits__(self):
        print (f"Le nombre de crédits de {self.__prenom} {self.__nom} est de {self.__credits}")
        return self.__credits
    
    def __studentEval__(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 70:
            return "Très bien"
        elif self.__credits >= 60:
            return "Passable"
        elif self.__credits < 60:
            return "Insuffisant"
    
        
    def __student_Info__(self):
        print (f"Prénom = {self.__prenom}\n Nom = {self.__nom}\n Id = {self.__numero_etudiant}\n Niveau = {self.__level}")
        return self.__prenom, self.__nom, self.__level, self.__numero_etudiant
    
John_Doe = Student("Doe","John",145)

John_Doe.__add_credits__(10)
John_Doe.__add_credits__(10)
John_Doe.__add_credits__(50)
John_Doe.__get_credits__()
print (John_Doe.__studentEval__())
John_Doe.__student_Info__()