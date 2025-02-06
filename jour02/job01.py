class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur
    def get_largeur(self):
        return self.__largeur

    def set_longueur(self,longueur):
        self.__longueur = longueur
    def set_largeur(self,largeur):
        self.__largeur = largeur


forme = Rectangle(10, 5)
print(f"Le rectangle a {forme.get_longueur()} en longueur et {forme.get_largeur()} en largeur")
 


forme.set_longueur(100)
forme.set_largeur(50)
print(f"Le rectangle a {forme.get_longueur()} en longueur et {forme.get_largeur()} en largeur")
