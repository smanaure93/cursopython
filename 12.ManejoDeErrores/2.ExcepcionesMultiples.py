while (True):
    try:
        Num = int(input("Ingresa un numero: "))
        print(100 / Num)
        break
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
    except ValueError:
        print("Debes ingresar un número entero")
    except KeyboardInterrupt:
        print("\n Finalizada la ejecución")
        break
