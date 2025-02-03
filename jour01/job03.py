class Operator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    def Addition(self):
        return(self.number1 + self.number2)

value = Operator( 1, 2)
result = value.Addition()

print(f"Le résultat est : {result}")
