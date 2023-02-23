'''
Escribe un programa que pida dos palabras y diga si riman o no.
Si coinciden las tres últimas letras tiene que decir que riman. 
Si coinciden sólo las dos últimas tiene que decir que riman un poco y si no, que no riman.
extraño <--> tamaño
desligo <--> amigo
riman <--> cuerpo
sol <--> lol
lo <--> yo
'''

firstWord = input("Ingresa la primer palabra: ")
secondWord = input("Ingresa la segunda palabra: ")

if len(firstWord) < 3 or len(secondWord) < 3:
    print("NO rima, porque tienen menos de 3 caracteres")
elif firstWord[-3:] == secondWord[-3:]:
    print("Las palabras riman")
elif firstWord[-2:] == secondWord[-2:]:
    print("Las palabras riman un poco")
else:
    print("Las palabras no riman")
