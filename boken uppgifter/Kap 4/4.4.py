högt = int(input("Skriv högtet: "))
i = 0

while högt > 0.01:
    print(f"{i} gång. Högt är {högt:.2f}. ", end=" ")
    högt *= 0.7
    i += 1
    print(f"Nu är det {högt:.2f} meter", end="\n")
else:
    print(f"Ballen är stilla på golvet efter {i} gånger")
    