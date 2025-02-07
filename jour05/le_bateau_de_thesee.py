class Part:
    def __init__(self, piece, materiaux):
        self.piece = piece
        self.materiaux = materiaux

    def chang_materiaux(self, nouveau_materiaux):
        self.materiaux = nouveau_materiaux

    def __str__(self):
        return (f"Le {self.piece} est fabriquée en {self.materiaux}")


bato = Part("mât", "bois") 
print(bato.__str__())

