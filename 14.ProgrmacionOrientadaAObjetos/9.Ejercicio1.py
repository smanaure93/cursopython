'''
Realizar un programa que conste de una clase llamada Estudiante, 
que tenga como atributos el nombre y la nota del alumno. 
Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje 
con el resultado de la nota y si ha aprobado o no.
'''

class Student():
    def __init__(self, name, grade):
        self.__name = name
        self.__grade = grade

    @property
    def name(self):
        return self.__name

    @property
    def grade(self):
        return self.__grade

    def isApproved(self):
        if self.__grade < 10:
            print('Has reprobado con: {} puntos'.format(self.__grade))
        else:
            print('Has aprobado con: {} puntos'.format(self.__grade))


name = input('Nombre: ')
grade = int(input('Nota: '))

student = Student(name, grade)
print(student.name)
print(student.grade)
student.isApproved()
