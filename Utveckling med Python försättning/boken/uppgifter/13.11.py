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

    # metoder för att jämföra objeketer på samma klassen

    # == lika
    def __eq__(self, other):
        return self._r == other._r
    
    # < minre än
    def __lt__(self, other):
        return self._r < other._r

    # <= minre eller lika än
    def __le__(self, other):
        return self._r <= other._r

    # > högre än
    def __gt__(self, other):
        return self._r > other._r

    # <= högre eller lika än
    def __ge__(self, other):
        return self._r >= other._r

c1 = Cirkel(1,1,4)
c2 = Cirkel(1,3,4)
c3 = Cirkel(4,5,3)

print(c1 == c2, c2 >= c3, c3 < c1)
