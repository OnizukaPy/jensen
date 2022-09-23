import random

# beteckna två randoma heltal m och n där m > n
while True:

    temp_m = random.randint(1, 1000)
    temp_n = random.randint(1, 1000)

    if temp_m != temp_n and temp_m > temp_n:
        m = temp_m
        n = temp_n
        print("m", m, "och n", n)
        break
    elif temp_m != temp_n and temp_m < temp_n:
        m = temp_n
        n = temp_m
        print("m", m, "och n", n)
        break

# bräkna SGD
old_m = m
old_n = n

while True:
    r = m % n
    if r == 0:
        print(f"{n} är SDG mellan {old_m} och {old_n}")
        break
    elif r != 0:
        m = n
        n = r

    

        

