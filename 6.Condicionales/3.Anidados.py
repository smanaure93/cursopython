name = input("Ingresa tu nombre: ")
age = int(input("Ingresa tu edad: "))

if name == "Sócrates":
    if age >= 18:
        print("Eres Sócrates y tienes mayoria de edad")
    else:
        print('Eres Sócrates, pero, NO tienes mayoria de edad')
else:
    print("Tu NO eres Sócrates")
