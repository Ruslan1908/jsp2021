import math

class Kolo():
    pi=math.pi
    def __init__(self, r):
        self.r = r
    def pole(self):
        print("Pole koła wynosi:", round(self.pi*(self.r**2), 2), "cm^2")
    def obwod(self):
        print("Obwód koła wynosi:", round(2*self.pi*self.r, 2), "cm")

r = float(input("Podaj promień koła: "))

promien = Kolo(r)

promien.pole()
promien.obwod()
