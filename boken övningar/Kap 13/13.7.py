from math import pi, sqrt

class Punkt:

    def __init__(self, namn, x, y):
        self.namn = namn
        self.x = x 
        self.y = y

class Figure:

    def __init__(self, namn):
        self.namn = namn
    
class Cyrkel(Figure):

    def __init__(self, namn, r):
        super().__init__(namn)
        self.radie = r
    
    def area(self):
        return (self.radie**2)*pi

class Rektangel(Figure):
    # startpunkt är den punkten i botten till vänster och p2 är den punkten i toppen till höger
    def __init__(self, namn, startpunkt, p2):
        super().__init__(namn)
        self.x = startpunkt.x
        self.y = startpunkt.y
        self.x2 = p2.x
        self.y2 = p2.y
    
    def area(self):
        return (self.x2 - self.x)*(self.y2 - self.y)

class Triangel(Figure):

    def __init__(self, namn, startpunkt, p2, p3):
        super().__init__(namn)
        self.x = startpunkt.x
        self.y = startpunkt.y
        self.x2 = p2.x
        self.y2 = p2.y
        self.x3 = p3.x
        self.y3 = p3.y

    def area(self):
        xm_1_2 = (self.x + self.x2) / 2
        ym_1_2 = (self.y + self.y2) / 2
        dist_1_2 = sqrt((self.x2 - self.x)**2 + (self.y2 - self.y)**2)
        dist_3_pm_1_2 = sqrt((self.x3 - xm_1_2)**2 + (self.y3 - ym_1_2)**2)
        
        return (dist_1_2 * dist_3_pm_1_2) / 2

startpunkt = Punkt("A", 1,1)
p2 = Punkt("D", 2,2)
p3 = Punkt("B", 1,2)

rek = Rektangel("ABCD", startpunkt, p2)
tri = Triangel("ABC", startpunkt, p2, p3)
print("\n")
print(f"Rektangel {rek.namn}s area är: {rek.area():.2f}")
print(f"Triangel {tri.namn}s area är: {tri.area():.2f}")
print("\n")

