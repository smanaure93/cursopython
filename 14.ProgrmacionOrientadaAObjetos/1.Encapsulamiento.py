class A():
    def __init__(self):
        self.counter = 0
    
    def add(self):
        self.counter += 1
    
    def count(self):
        return self.counter

class B():
    def __init__(self):
        self.__counter = 0
    
    def add(self):
        self.__counter += 1
    
    def count(self):
        return self.__counter

print("Objeto 1")

a = A()
print(a.count())
a.add()
print(a.count())
print(a.counter)

print("Objeto 2")
b = B()
print(b.count())
b.add()
b.add()
print(b.count())