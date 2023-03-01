'''
Pedir al usuario que ingrese 2 numeros, después, se debe mostrar el rango de esos 2 números, pero,
solo imprimiendo los números que sean impares
'''

firstValue = int(input("Ingrese la primera cifra: "))
secondValue = int(input("Ingrese la segunda cifra: "))

for i in range(firstValue, secondValue + 1):
    if i % 2 != 0:
        print(i)
