"""
Con el siguiente diccionario, debes crear un programa que pregunte al usuario por un número;
el programa debe imprimir el jugador al que hace referencia ese número
"""
diccionario = {
    1 : "Casillas", 15 : "Ramos",

    3 : "Pique", 5 : "Puyol",

    11 : "Capdevila", 14 : "Xabi Alonso",

    16 : "Busquets", 8 : "Xavi Hernandez",

    18 : "Pedrito", 6 : "Iniesta",

    7 : "Villa"
}

userInput = int(input("Ingrese un número de jugador: "))

if userInput in diccionario:
    print(diccionario[userInput])
else:
    print("Jugador no encontrado")

