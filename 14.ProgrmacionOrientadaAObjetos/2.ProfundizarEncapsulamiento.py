class A():
    def __init__(self):
        self._counter = 0
        self._count = 0

    def add(self):
        self._counter += 1

    def multiply(self, multiplier):
        self._counter = self._counter * multiplier

    def count(self):
        return self._counter


a = A()
a.add()
a.add()
a.multiply(2)
print(a.count())
