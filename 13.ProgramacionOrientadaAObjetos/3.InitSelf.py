class FabricaTelefonos():
    def __init__(self, marca, color):
        self.marca = marca
        self.color = color


telefono = FabricaTelefonos('Xiaomi', 'negro')
print(telefono.marca)
print(telefono.color)
