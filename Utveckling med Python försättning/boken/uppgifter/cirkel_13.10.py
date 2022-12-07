from math import pi

class Cirkel:
    def __init__(self, x=0, y=0, radie=0):
        self.x = x
        self.y = y
        self.r = radie
    
    # för att kolla automatisk och utan att göra andra metoder, man kan anropa @property sättet.
    # i det här sättet klassen anropa automatisk t.ex att radie är inte negativa direkt i instansvariabel
    # när den är avcallad i coden.
    @property 
    def r(self):
        return self._r 

    @r.setter
    def r(self, r):
        assert r >= 0, ('Negative radie', r)
        self._r = r
    
    def area(self):
        return pi * self.r**2

    def omkr(self):
        return 2*pi*self.r

    @property
    def arean(self):
        return pi * self.r**2
    
    @property
    def omkretsen(self):
        return 2*pi*self.r


c = Cirkel(radie=2)

print(f"Area: {c.area():.2f} och omkr: {c.omkr():.2f}")
print(f"Area: {c.arean:.2f} och omkr: {c.omkretsen:.2f}")

