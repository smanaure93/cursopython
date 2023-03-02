class PhoneFactory():
    brand = "Xiaomi"
    color = "black"
    ramMemory = 32
    romMemory = 128

    def makeCall(self, msg):
        return msg.upper()

    def listenToMusic(self):
        print("Estás escuchando música")


phone = PhoneFactory()
print(phone.brand)
print(phone.color)
print(phone.ramMemory)
print(phone.romMemory)

print(phone.makeCall("¿Hay alguien ahí?"))
phone.listenToMusic()
