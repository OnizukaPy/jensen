# sätt in ett antal
n = int(input("Sätt n: "))

# skapa en lista med längden n+1 och den första element är False och alla övriga elementer är Treu
list_bool = [False] * (n+1)
for i in range(1, len(list_bool)):
    list_bool[i] = True

# löp igenom lista med början på index 2
for i in range(2, len(list_bool)):
    # när man stöter på ett element som är True i platsen i 
    if list_bool[i] == True:
        # löp igenom resten av listan  och sätt varje elementer som har egenskapen att 
        # dess index är en jämn multipel av i till False
        for j in range(i+1, len(list_bool)):
            if j%i == 0:
                list_bool[j] = False

print("\n")

for i in range(len(list_bool)):
    if list_bool[i] == True:
        print(i, end=" ")

print("\n")
