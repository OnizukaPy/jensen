import random

def medel(v):
    m = sum(v)/len(v)
    return m

n = random.randint(0, 100)
ll = []
for i in range(0, n):
    ll.append(random.randint(-n, n))

lt = tuple(ll)

print(f"Medel från lista: {medel(ll):.2f} och Medel från tuple: {medel(lt):.2f}")

