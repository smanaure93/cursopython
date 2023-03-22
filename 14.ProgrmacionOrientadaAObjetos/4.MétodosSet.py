class A():
    def __init__(self):
        self._count = 0
        self._counter = 0

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, count):
        self._count = count

    @property
    def counter(self):
        return self._counter

    @counter.setter
    def counter(self, counter):
        self._counter = counter


a = A()

print(a.count)
a.count = 20
print(a.count)
print(a.counter)
a.counter = 10
print(a.counter)
