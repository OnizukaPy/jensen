# antalet siffrorna i heltal

def count(n):
    l = []
    while n>0:
        rest = n % 10
        l.append(rest)
        n = n // 10
    return len(l)

while True:
    try:
        heltal = int(input("Skriv ett heltal: "))
        print("\n")
        if heltal > 0: 
            print(f"heltalet har {count(heltal)} siffror\n")
            break
        elif heltal < 0:
            print("Talet är < 0, en gång till\n")
    except ValueError:
        print("Talet är inte en heltal, en gång till\n")
    




