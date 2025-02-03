class People:
    def __init__(self,name, lastname):
        self.name = name
        self.lastname = lastname

    def Introduce (self):
        return (f"I am {self.name} {self.lastname}")
    
name1 = People("John", "Doe")
name2 = People("Jean","Dupond")

print(name1.Introduce())
print(name2.Introduce())