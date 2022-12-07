from math import pi

class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.set_r(radie)
    
    def get_r(self):
        return self._r 

    def set_r(self, r):
        assert r >= 0, ('Negative radie', r)
        self._r = r
    
    def area(self):
        return pi * self._r**2

    def omkr(self):
        return 2*pi*self._r


c = Cirkel()
c.set_r(3)
print(f"Area: {c.area():.2f} och omkr: {c.omkr():.2f}")
print(c._r)
