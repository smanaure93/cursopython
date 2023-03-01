'''
Escribir un programa que pida un numero al usuario y muestre las tablas de multiplicar de ese numero
'''
userInput = int(input("Ingresa un numero para saber su tabla: "))
i = 0
result = 0

while i <= 10:
    result = userInput * i
    print("{} x {} = {}".format(userInput, i, result))
    i += 1
