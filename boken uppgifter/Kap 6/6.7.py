# Inläsning till en matris
print(  " Skriv en matris rad för rad. "
        "Avsluta med en tom rad.")

m = []
while True:
    s = input("? ")
    if s == "":
        break

    ls = s.split(",")
    rad = [float(e) for e in ls]
    m.append(rad)

print(m)
