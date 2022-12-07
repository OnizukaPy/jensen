from math import pi

class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.set__r(radie)
    
    def get__r(self):
        return self.__r 

    def set__r(self, r):
        assert r >= 0, ('Negative radie', r)
        self.__r = r
    
    def area(self):
        return pi * self.__r**2

    def omkr(self):
        return 2*pi*self.__r


c = Cirkel()
c.set__r(1)
print(f"Area: {c.area():.2f} och omkr: {c.omkr():.2f}")
print(c.__r)
