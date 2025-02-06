class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages


    def get_titre(self):
        return self.__titre
    def get_auteur(self):
        return self.__auteur
    def get_pages(self):
        return self.__pages

    def set_titre(self,titre):
        self.__titre = titre
    def set_auteur(self,auteur):
        self.__auteur = auteur
    def set_pages(self,pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("Le nombre de pages doit un entier positif")


roman = Livre("1984", "George Orwell", 482) 
print(f"Le titre est {roman.get_titre()}, l'auteur est {roman.get_auteur()}, et possède {roman.get_pages()} pages.")


roman.set_titre("Dune Tome 1")
roman.set_auteur("Krank Herbert")
roman.set_pages(832)
print(f"Le titre est {roman.get_titre()}, l'auteur est {roman.get_auteur()}, et possède {roman.get_pages()} pages.")
