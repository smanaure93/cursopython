'''
Escribe una lista que tenga los números de 1 al 10. Luego, debes hacer que los datos que están
en las posiciones 4, 7 y 9 sean multiplicados por 2; por último, 
mostrar la lista nueva con los nuevos datos
'''

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list[3] *= 2
list[6] *= 2
list[8] *= 2

print("El resultado de la lista es: {}".format(list))
