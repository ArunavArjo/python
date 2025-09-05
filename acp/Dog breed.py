class Dog:

    species = 'Dog'

    def __init__(self,name,age):
        self.name = name
        self.age = age
        

pipo = Dog("Pipo","9",)
naruto = Dog("Naruto","8")
print(f"Pipo is a {pipo.species}")
print(f"Naruto is a {naruto.species}")
print("{} is {} year old" .format(pipo.name,pipo.age))
print("{} is {} year old" .format(naruto.name,naruto.age))