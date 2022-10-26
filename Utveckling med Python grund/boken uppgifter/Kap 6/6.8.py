# Skapa en 10 x 10 multilikationstabell
n = int(input("Skriv den övre gränsen av multiplikationstabell: "))
a = []
for i in range(0, n):
    a.append([])
    for j in range (0, i+1):
        a[i].append((i+1)*(j+1))
    #print(" ".join([str(x).rjust(3) for x in a[i]]))

# beräkning av maximun nummer av tecken varie cifra
maxx = []
for i in range(len(a)):
    for j in range(len(a[i])):
        b = str(a[i][j])
        maxx.append(len(b))

maxx = max(maxx)

# utskriften av tabell där alla cifror är justifierad
print("\n")

# skapa lista av columnstal
column_t = []
for i in range(len(a)):
    column_t.append(i+1)

print(str("").rjust(maxx)+" ", " ".join([str(x).rjust(maxx) for x in column_t]))
print("\n")

# skapa tabellen justifierad
for i in range(len(a)):
    print(str(i+1).rjust(maxx)+")", " ".join([str(x).rjust(maxx) for x in a[i]]))
print("\n")