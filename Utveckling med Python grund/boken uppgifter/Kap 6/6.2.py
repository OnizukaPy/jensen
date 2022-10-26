import random

n = random.randint(1, 100)
tal_lista = []
for i in range(n):
    tal_lista.append(random.randint(-n, n))

print(f"Tals lista är: {tal_lista}")
c = 0
for i in tal_lista:
    if i < 0:
        c += 1

print(f" Det finns {c} tal som är negativa")