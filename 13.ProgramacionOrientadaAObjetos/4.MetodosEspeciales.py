class PhoneFactory():
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
        print("El objeto {} ha sido creado".format(self.brand))

    def __str__(self):
        return "El objeto es {}".format(self.brand)

    def __del__(self):
        print("El objeto {} ha sido destruido".format(self.brand))


phone = PhoneFactory("Nokia", "Negro")
print(phone.brand)
print(phone)
