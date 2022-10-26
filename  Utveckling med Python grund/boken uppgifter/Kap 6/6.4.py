import random

tal_lista = []
n = random.randint(1, 100)

for i in range(n):
    tal_lista.append(random.randint(0, 10))

print("\n")
print(tal_lista, "\n")

if tal_lista.count(0) != 0:
    print(f"Det finns {tal_lista.count(0)} noll i listan\n")
    for i in range(len(tal_lista)):
        if 0 in tal_lista:
            tal_lista.remove(0)
        else:
            continue
    print(tal_lista, "\n")
else:
    print("Det finns inte noll i listan\n")


