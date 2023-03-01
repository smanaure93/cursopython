'''
Crear una funcion que pida dos numeros. Si el primero es mayor al segundo, 
el programa debe retornar el valor 1; si el segundo es mayor al primero, debe retornar -1;
si ambos son iguales, debe retornar 0
'''


def comparation():
    firstValue = float(input("Ingrese un valor: "))
    secondValue = float(input("Ingrese un valor: "))
    if firstValue > secondValue:
        return 1
    elif firstValue < secondValue:
        return -1
    else:
        return 0


print(comparation())
