

def är_perfekt(n):
    temp = []
    for i in range(1, n):
        if n % i == 0:
            temp.append(i)

    if sum(temp) == n:
        return True
    else:
        return False

while True:
    
    try:
        heltal = int(input("\nSkriv ett heltal: "))
        if heltal < 0:
            print("\nDu har skrivit fel. Talet måste vara >= 0. en gång till\n")
        else:
            print(f"\nÄr {heltal} ett perfekt tal? {är_perfekt(heltal)}\n")
            break
    except ValueError:
        print(f"\nDu har skrivit inte ett heltal. En gång till\n")
