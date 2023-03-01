"""
Crear un programa que tenga una lista, luego crear una funcion con la cual se van a pedir numeros al
usuario para agregar a la lista. Debes crear una segunda funcion en donde se ordenen los numeros pares 
e impares dentro de dos listas nuevas
"""
list = []

def askNumbers():
    i = 0
    while i < 5:
        num = float(input("Ingresa un número para la lista: "))
        list.append(num)
        i += 1
    print("Lista completa: ", list)


def sortList():
    list.sort()
    pairs = []
    odds = []
    for i in list:
        if(i % 2 == 0):
            pairs.append(i)
        else:
            odds.append(i)
    print("Pares: ", pairs)
    print("Impares: ", odds)

askNumbers()
sortList()