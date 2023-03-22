class Animal():
    def __init__(self , mensaje):
        self.mensaje = mensaje

    def speak(self):
        print(self.mensaje)

class Dog(Animal):
    def speak(self):
        print("Yo hago Guau!")

class Fish(Animal):
    def speak(self):
        print("Yo no hablo")

dog = Dog("Guau!")
dog.speak()

animal = Animal("Miau!")
animal.speak()

fish = Fish("Nada")
fish.speak()