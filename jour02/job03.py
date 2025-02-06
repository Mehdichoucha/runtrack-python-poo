class Livre:
    def __init__(self, disponible):
        self.__disponible = disponible

    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print(f"le livre a été emprunter")
        else:
            print(f"le livre n'est pas disponible")

    def rendre(self):
        if not self.verification():
            self.__disponible = True
            print(f"le livre est disponible")
        else:
            print(f"le livre a été rendu")


roman = Livre(True)
print(roman.verification())
roman.emprunter()
roman.emprunter()
roman.rendre()
print(roman.verification())