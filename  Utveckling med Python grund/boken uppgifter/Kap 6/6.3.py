import random

tal_lista = []
n = random.randint(1, 100)

for i in range(n):
    tal_lista.append(random.randint(1, 1000))

min_talet = min(tal_lista)
max_talet = max(tal_lista)
medelvärde = float(sum(tal_lista)/n)

print(f"Min: {min_talet}, Max: {max_talet}, Medelvärde: {medelvärde:.2f}")

