'''
Realizar un programa que haga el proceso de formula general para la resolución de ecuaciones,
sabiendo que la formula general es la que está en la imagen, el usuario debe ingresar los valores de “a”,
“b” y “c”, y el programa debe hacer el proceso para que al final muestre el mensaje:
“La solución es: <solucion>”
x = ((-b +- sqrt(b**2 - 4ac)) / 2a)
'''
# Se importa la raíz cuadrada
from math import sqrt

# Se declara el input para cada variable
A = int(input("Ingresa el valor de A: "))
B = int(input("Ingresa el valor de B: "))
C = int(input("Ingresa el valor de C: "))

# Variables de resultado
x1 = 0
x2 = 0

# Realizamos el cálculo de la parte interna de la raíz cuadrada
insidesqrt = (B**2) - (4*A*C)

# Por la división, A no puede ser 0
if (A == 0):
    print("El valor de A no puede ser 0")
# No se pueden calcular raices cuadradas de números negativos
elif (insidesqrt < 0):
    print("No se puede realizar porque no se puede sacar raiz a un numero negativo")
# Valores validos
else:
    x1 = ((B*-1) + sqrt(insidesqrt)) / (2*A)
    x2 = ((B*-1) - sqrt(insidesqrt)) / (2*A)
    print("La solucion es: \nx1=", round(x1, 2), "\nx2=", round(x2, 2))
