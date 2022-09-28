def nfak(n):
    tal_list = []
    if n > 0:
        for i in range(1, n+1):
            tal_list.append(i)
        #print(tal_list)
        fak = 1
        for i in range(len(tal_list)):
            fak = fak * tal_list[i]
        return fak
    elif n == 0:
        return 1
    
while True:
    try:
        heltal = int(input("Skriv ett heltal: "))
        print("\n")
        if heltal < 0:
            print("\nDu har skrivit fel. Talet måste vara >= 0. en gång till\n")
        else:
            print(nfak(heltal))
            break
    except ValueError:
        print(f"\nDu har skrivit inte ett heltal. En gång till\n")
