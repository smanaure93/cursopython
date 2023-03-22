class A():
    def first(self):
        return "Esta es la clase A"


class B():
    def second(self):
        return "Esta es la clase B"


class C(A, B):
    pass


c = C()
print(c.first())
print(c.second())
