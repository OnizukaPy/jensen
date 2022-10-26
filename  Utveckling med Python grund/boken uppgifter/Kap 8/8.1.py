from cmath import pi

def area(r):
    return pi*r**2

def omkrets(r):
    return 2*pi*r

radie = float(input("Skriv cirkelns radie: "))
print("\n")

print(f"Area: {area(radie):.2f} och Omkrets: {omkrets(radie):.2f}\n")