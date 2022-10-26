import random

# att skapa en randomisk heltals lista
tal_lista = []
n = random.randint(1, 100)

for i in range(n):
    tal_lista.append(random.randint(-n, n))

print("\n")
print(len(tal_lista))
print("\n")
print(tal_lista)
print("\n")

tal_lista_2 = []

for i in tal_lista:
    for t in range(tal_lista.index(i)+1, len(tal_lista)):
        if tal_lista[t] == i:
            print(f"talet {i}, i platsen {tal_lista.index(i)} uppreppas i platsen {t}")

# om ett tal uppreppas det betyder att det är i listan mellan talsindex och början.
for i in range(1, len(tal_lista)):
    if tal_lista[i] not in tal_lista[:i]:
        tal_lista_2.append(tal_lista[i])

print("\n")
print(len(tal_lista_2))
print("\n")
print(tal_lista_2)
print("\n")
