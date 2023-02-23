'''
En la siguiente lista, debes hacer un programa que muestre los valores al usuario, a su vez,
debe pedir dos datos y esos que sean ingresados deben ser sustituidos en el primer y segundo lugar:

[20, 50, "Curso", 'Python', 3.14]
'''

list = [20, 50, "Curso", 'Python', 3.14]

userInput = input("Ingresa el valor a sustituir en la primera posición: ")
list[0] = userInput

userInput = input("Ingresa el valor a sustituir en la segunda posición: ")
list[1] = userInput

print("El valor de la lista es el siguiente: \n{}".format(list))
