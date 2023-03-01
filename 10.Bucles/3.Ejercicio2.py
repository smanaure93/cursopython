'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla 
todos los años que ha cumplido (desde 1 hasta su edad).
'''
age = int(input("Digita tu edad, para mostrarte tus años: "))
i = 1

while i <= age:
    if(i == 1):
        print("Has cumplido: {} año".format(i))
    else:
        print("Has cumplido: {} años".format(i))
    i += 1
