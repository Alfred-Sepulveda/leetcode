
class Animal:
    def __init__(self):
        print("ANIMAL CREATED")
    def who_am_i(self):
        print("I am an animal")
    def eat(self):   #this is original atttribute but gets overwritten in DogCLass
        print("I am eating")

class Dog(Animal):   # this will inherit class Animal
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created")
    def eat(self):   #this will print instead of inherit class attribute of Animal
        print("I am a dog and eating")
    def bark(self):
        print("WOOF!")

mydog = Dog()
mydog.bark()
mydog.eat()



    