class Animal():
    def speak(self):
        print("Estoy hablando")

    def description(self):
        print("Yo soy un {}".format(self.animal))


class Dog(Animal):
    pass


class Gato(Animal):
    def __init__(self, animal):
        self.animal = animal


animal = Animal()
animal.speak()

dog = Dog()
dog.speak()

gato = Gato("Gato")
gato.description()
