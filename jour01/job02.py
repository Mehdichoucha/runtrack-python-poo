class Operator:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

value = Operator( 1, 2)

print(f"Le nombre 1 est : {value.number1}")
print(f"Le nombre 2 est : {value.number2}")