class A():
    def __init__(self):
        self._count = 0
        self._counter = 0

    @property
    def count(self):
        return self._count

    @property
    def counter(self):
        return self._counter


a = A()

print(a.count)
print(a.counter)
