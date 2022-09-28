from cmath import pi

def cirklel(r):
    area = pi*r**2
    omkrets = 2*pi*r
    return (area, omkrets)


radie = float(input("Skriv cirkelns radie: "))
print("\n")

print(f"Area: {cirklel(radie)[0]:.2f} och Omkrets: {cirklel(radie)[1]:.2f}\n")