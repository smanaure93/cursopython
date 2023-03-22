class Animal():
    def __init__(self , name):
        self.name = name

class Dog(Animal):
    def __init__(self , name , sound):
        super().__init__(name)
        self.sound = sound

dog = Dog("Scooby" , "Woof!")
print(dog.name)
print(dog.sound)