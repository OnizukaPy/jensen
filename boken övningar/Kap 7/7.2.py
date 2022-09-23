# Algoritm gör den följende operationer:
#  - det läser in talet
#  - det delar varje tal för en lista av tal som är faktor
#  - tillstist det jämföra summa sv faktorer med talet, om de är lika skriver det ut "Det talet är perfelt!.

print("\n")
n = int(input("Skirv det max talet: "))
print("\n")
for i in range(1, n):
    temp = []
    for j in range(1, i):
        if i % j == 0:
            temp.append(j)
    
    if sum(temp) == i:
        print(f"{i} är ett perfekt tal!")
    
print("\n")