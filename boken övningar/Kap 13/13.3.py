import math

class Punkt:

    def __init__(self, p, x, y):
        self.p = p
        self.x = x 
        self.y = y
        self.old_x = x
        self.old_y = y

    def dist_from_zero(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def flytta_hor(self, x1):
        self.x += x1

    def flytta_ver(self, y1):
        self.y += y1

    def get_coord(self):
        return f"{self.p}{(self.x, self.y)}"    

class Dist_punkt:

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def get_distance(self):
        return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
print("\n")
p1 = Punkt("A", 1,2)
print(p1.get_coord())
p2 = Punkt("B", 2,6)
print(p2.get_coord())
distance = Dist_punkt(p1, p2)
print(f"Avståndet mellan {p1.p} och {p2.p} är: {distance.get_distance():.2f}")

print("\n")
print(f"Avståndet mellan 0 och p1: {p1.dist_from_zero():.2f}")
print(f"Avståndet mellan 0 och p2: {p2.dist_from_zero():.2f}")

print("\n")
p1.flytta_hor(-3)
p1.flytta_ver(4)
print(p1.get_coord())
print(f"Avståndet mellan 0 och ny p1: {p1.dist_from_zero():.2f}")