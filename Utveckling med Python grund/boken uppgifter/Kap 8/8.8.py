import random

def byt_elem(a, låg, högre, värde):
    for i in range(låg, högre+1):
        lista[i] = värde
    return lista


n = random.randint(11, 100)
lista = []
for i in range(n):
    lista.append(random.randint(-n, n))

print(lista)
print(byt_elem(lista, 2, 6, "OK"))