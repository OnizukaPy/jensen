import random

n = random.randint(1, 100)
talföljd = []
k = 3
for i in range(n):
    talföljd.append(i*k)

print(f"\nJag har valt {n} tal. Kostant i geomtriska talföljdet är {k}\n")
print(f"Talföljdet är: {talföljd}")