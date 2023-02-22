'''
Escribir un programa que solicite al usuario una vocal en minuscula, y luego una letra en mayúsculas.
El programa debe convertir la letra en minúscula y la vocal en mayúscula, y al final, 
deben ser concatenadas ambas
'''

lowerCharacter = input("Ingresa una LETRA EN MINUSCULA: ")
upperCharacter = input("Ingresa una LETRA EN MAYUSCULA: ")

lowerCharacter = lowerCharacter.upper()
upperCharacter = upperCharacter.lower()

print("La primera letra fue: {} \nLa segunda letra fue: {}".format(
    lowerCharacter, upperCharacter))
