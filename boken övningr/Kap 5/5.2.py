# Skriv ett program som läser in ett personnummer och skriver ut meddelandet: Grattis! om
# den aktuella personen har födelsedag
# Personnummer anges med 10 sifror (utan minustecken)

check = 0
while True:
    
    text = input("Skriv ditt personnummer 10 cifror: \n> ")
    temp = text.strip().lower()
    # check av minus
    for t in temp:
        if t == "-":
            check = 1
    if len(text) == 10:
        print("\nOK, perfekt personnummer är skrivit rätt.\n")
        break
    elif len(text) > 10 and check == 1:
        print("\nNEJ, du måste inte skriva minus mellan nummrar.\nen gång till snälla")
        check = 0
    else:
        print("\nNEJ, kanske har du skrvit mer eller minre cifror.\n")

# check av personnummer är rätt för skatteverket
# https://sv.wikipedia.org/wiki/Personnummer_i_Sverige

udda = ""
jämn = ""
for i in range(0, len(temp)-1, 2):
    jämn += str(int(temp[i])*2)
    #print(jämn)
for i in range(1, len(temp)-2, 2):
    udda += str(int(temp[i]))
    #print(udda)

temp2 = jämn + udda
#print(temp2)
summa = 0
for i in temp2:
    summa += int(i)

check_sum = (10 - (summa%10)) % 10
#print(check_sum)

if check_sum == int(temp[-1]):
    print("Personnummer är rätt för skatteverket\n")
else:
    print("Personnummer är inte rätt för skatteverket\n")



# check för födelsedag
import datetime as dt

idag = str(dt.datetime.now().date()).replace("-", "")[2:] # idag skrivit som sträng av 6 cifror

if idag in temp:
    print("Grattis! Idag är ditt födelsedag!\nHejdå!\n")
else:
    print("Tyvärr idag är inte ditt födelsedag!\nHejdå!\n")