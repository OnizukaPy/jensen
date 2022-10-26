while True:

    text = input("Skriv text pytonorm: ")

    if text != "pytonorm":
        print("\nEn gång till, du har skrivit fel\n")
    else:
        break

ord1 = text[2:5]
ord2 = text[4:]
ord3 = text[-4:-7:-1]

print(f"Ord n1: {ord1}. Ord n2: {ord2}. Ord n3: {ord3}")
