import random

def udda(t):
    return t % 2 != 0

n = random.randint(1, 100)
lista = []
for i in range(n):
    lista.append(random.randint(-n, n))

print("\n")
print(lista)
print("\n")

w = list(filter(udda, lista))

print("\n")
print(w)
print("\n")

d = list(filter(lambda x : x % 2 != 0, lista))

print("\n")
print(d)
print("\n")