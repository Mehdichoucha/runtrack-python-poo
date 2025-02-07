class Student:
    def __init__(self, nom, prénom, numéro, crédit):
        self.__nom = nom
        self.__prénom = prénom
        self.__numéro = numéro
        self.__crédit = crédit

    def get_nom(self):
        return self.__nom
    def get_prénom(self):
        return self.__prénom
    def get_numéro(self):
        return self.__numéro
    def get_crédit(self):
        return self.__crédit

    def set_nom(self,nom):
        self.__nom = nom
    def set_prénom(self,prénom):
        self.__prénom = prénom
    def set_numéro(self,numéro):
        self.__numéro = numéro
    def set_crédit(self,crédit):
            self.__crédit = crédit


    def add_credits(self):
        if ajout_credit.crédit > 0:
            self.crédit = self.crédit + ajout_credit.crédit
        else:
            return ("Nombre des crédit insuffisant")







ajout_credit = Student("Doe", "John", 145, 50)
print(f"Le nombre de crédits de {ajout_credit.get_nom()} {ajout_credit.get_prénom()} est de {ajout_credit.get_crédit()}")

ajout_credit.set_crédit(500)
print(f"Le nombre de crédits de {ajout_credit.get_nom()} {ajout_credit.get_prénom()} est de {ajout_credit.get_crédit()}")

ajout_credit.set_crédit(-3)
print(f"Le nombre de crédits de {ajout_credit.get_nom()} {ajout_credit.get_prénom()} est de {ajout_credit.get_crédit()}")

