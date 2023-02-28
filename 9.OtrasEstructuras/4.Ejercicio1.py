"""
Escribir una tupla con los meses del año, luego, pide al usuario un numero, el que haya ingresado,
es el mes que debe mostrar en la tupla
"""

tupla = ('enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio',
         'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre')

month = int(input("Ingresa el numero de tu mes: "))

if month < 1 or month > 12:
    print("Debe introducir un valor valido")
else:
    print("Mes seleccionado: {}".format(tupla[month - 1].title()))
