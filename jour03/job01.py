class Ville:
    def __init__(self,nom,nombre_habitants):
        self.__nom = nom
        self.__nombre_habitants = nombre_habitants

    def get_nom(self):
        return self.__nom
    
    def get_nombre_habitants(self):
        return self.__nombre_habitants
    
    def set_nombre_habitants(self,nombre):
        self.__nombre_habitants = nombre
    

class Personne:
    def __init__(self,nom,age,ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouter_Population(self,):
        habitant = self.__ville.get_nombre_habitants()
        self.__ville.set_nombre_habitants(habitant + 1)


PARIS = Ville("Paris",1000000)
print(f"Population de la ville de {PARIS.get_nom()} : {PARIS.get_nombre_habitants()}.")
MARSEILLE = Ville("Marseille",861635)
print(f"Population de la ville de  {MARSEILLE.get_nom()} : {MARSEILLE.get_nombre_habitants()}.")

JOHN = Personne("John",45, PARIS)
MYRTILLE = Personne("Myrtille",4, PARIS)
CHLOÉ = Personne("Chloe",18, MARSEILLE)

JOHN.ajouter_Population()
MYRTILLE.ajouter_Population()
CHLOÉ.ajouter_Population()
print(f"Mise à jour de la population de la ville de {PARIS.get_nom()} : {PARIS.get_nombre_habitants()}.")
print(f"Mise à jour de la population de la ville de {MARSEILLE.get_nom()} : {MARSEILLE.get_nombre_habitants()}.")
