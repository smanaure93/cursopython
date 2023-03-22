'''
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando
el método __init__. Calcular después la suma, resta, multiplicación y división.
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
'''

class Calculator(): 
    def __init__(self, first, second):
        self.__first = first
        self.__second = second

    def addition(self):
        return self.__first + self.__second
    
    def substraction(self):
        return self.__first - self.__second
    
    def multiplication(self):
        return self.__first * self.__second
    
    def division(self):
        if self.__second == 0:
            return "No se pueden hacer division entre 0"
        else:
            return self.__first / self.__second
    
first = int(input('Primer valor: '))
second = int(input('Segundo valor: '))

calculator = Calculator(first, second)

print('Suma', calculator.addition())
print('Resta', calculator.substraction())
print('Multiplicación', calculator.multiplication())
print('División', calculator.division())