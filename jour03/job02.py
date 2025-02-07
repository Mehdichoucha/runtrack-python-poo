class Comptebanquaire:
    def __init__(self, compte, nom, prénom, solde):
        self.__compte = compte
        self.__nom = nom
        self.__prénom = prénom
        self.__solde = solde

    def afficher(self):
        return (f"Le n° de compte est {self.__compte}")
    
    def affichersolde(self):
        return (f"Le client {self.__prénom} {self.__nom} à une solde de {self.__solde}")



    def versement(self):
        self.__solde += 

    def retrait(self):


CLIENT = Comptebanquaire(12345, "Afton", "William", 654)
CLIENT2 = Comptebanquaire(12345, "Doe", "Nina", 654)