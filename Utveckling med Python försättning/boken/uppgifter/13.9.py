# ändra i din kalss Rektangel så att den får egenskaper (properties) h och b som beskriver höjden och bredden.
# Använd decorators (egenskaper)

class Rektanglel:
    def __init__(self, h, b):
        self.h = h
        self.b = b
    
    @property
    def area(self):
        return self.h * self.b

    @property
    def omkr(self):
        return 2*(self.h + self.b)

r = Rektanglel(2,3)
print(f"Area: {r.area:.2f} och omkr: {r.omkr:.2f}")