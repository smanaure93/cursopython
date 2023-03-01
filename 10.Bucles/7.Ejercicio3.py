'''
Imprimir por pantalla los numeros del 1 al 10, luego, pedir al usuario dos numeros y mostrar
el rango de numeros entre ambas cifras
'''

for i in range(1, 11):
    print(i)

firstValue = int(input("Ingrese la primera cifra: "))
secondValue = int(input("Ingrese la segunda cifra: "))

for i in range(firstValue, secondValue + 1):
    print(i)
