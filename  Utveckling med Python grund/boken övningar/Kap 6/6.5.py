import random
import math

while True:
    print("\n")
    n = int(input("skriv ett antal av tal: "))
    print("\n")
    if n > 0: break

# att skapa en tal lista längden n elementer
tal_lista = []
for i in range(n):
    tal_lista.append(random.randint(-n, n))
    print(tal_lista[i], end=" ")
print("\n")
# att beräkna medelvärden
m = sum(tal_lista)/n
print(f"\nMedelvärde är: {m}\n")

# att beräkna standardavvikelsen
rad = 0
for i in range(n):
    rad += pow(tal_lista[i]-m, 2)

s = math.sqrt(1/n * rad)

print(f"Standardavvikelsen är: {s}\n")