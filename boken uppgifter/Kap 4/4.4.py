höjd = int(input("Skriv höjden: "))
i = 0

while höjd > 0.01:
    print(f"{i} gång. Höjden är {höjd:.2f}. ", end=" ")
    höjd *= 0.7
    i += 1
    print(f"Nu är det {höjd:.2f} meter", end="\n")
else:
    print(f"Ballen är stilla på golvet efter {i} gånger")
    