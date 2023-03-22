'''
Crear una clase Fabrica que tenga los atributos de Llantas, Color y Precio;
luego crear dos clases mas que hereden de Fabrica, las cuales son Moto y Carro.
Crear metodos que muestren la cantidad de llantas, color y precio de ambos transportes.
Por ultimo, crear objetos para cada clase y mostrar por pantalla los atributos de cada uno
'''


class Factory():
    def __init__(self, tires, color, price):
        self.tires = tires
        self.color = color
        self.price = price


class Car(Factory):
    def info(self):
        return "\tLa cantidad de llantas del carro es: {}.\n\tEl color es: {}.\n\tEl precio es: {}".format(
            self.tires, self.color, self.price)


class Motorcycle(Factory):
    def info(self):
        return "\tLa cantidad de llantas de la moto es: {}.\n\tEl color es: {}.\n\tEl precio es: {}".format(
            self.tires, self.color, self.price)


car = Car(4, 'Negro', 25000)
motorcycle = Motorcycle(2, 'Rojo', 12000)

print("Carro:\n", car.info())
print("Moto:\n", motorcycle.info())
