class Dog():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says Woof!"

class Cat():
    def __init__(self,name):
        self.name = name
    
    def speak(self):
        return self.name + " says Meow!"

Fido = Dog("Fido")
print(Fido.speak())

Neko = Cat("Neko")
print(Neko.speak())

for pet in [Fido, Neko]: # here we have a function name but different signatures being used for different types
    print(type(pet))
    print(pet.speak())

def pet_speak(pet): 
    print(pet.speak())

pet_speak(Neko) # this is the same as print(Neko.speak()) Polymorphism


