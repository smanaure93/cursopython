"""
age = int(input("Ingrese su edad: "))
print("Tu edad es", age)
"""
while True:
    try:
        age = int(input("Ingrese su edad: "))
        print("Tu edad es", age)
        print("Se completó la ejecución")
        break
    except:
        print("Ingresaste un valor no válido, vuelva a intentar")
