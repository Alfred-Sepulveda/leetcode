

class Person():
    def insert(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum
    
    def output(self):
        print("Your name is " + self.name + ", your age is " + self.age + ", your ID is " + self.idNum)

p = Person()
p.insert('John', '121', '1234567890')
p.output()

class Person2():
    def __init__(self, name, age, idNum):
        self.name = name
        self.age = age
        self.idNum = idNum
    
    def output(self):
        print("Your name is " + self.name + ", your age is " + self.age + ", and your ID is " + self.idNum)

j = Person2('John', '118', '199')
j.output()
print(j.name)
print(j.age)
print(j.idNum)

class Man():
    def strong(self):
        print("Men are strong")


class Child(Person2, Man):
    pass

kid = Child('Lil John', '4', '2345')
kid.output()

kid.strong()


class Dog:
    def __init__(self, breed):
        self.breed = breed

bowser = Dog('English Bulldog')
print(bowser.breed)





