
while True:
    
    text = input("Skriv ditt personnummer 10 cifror med minus: \n> ")
    temp = text.strip().lower()
    index = temp.find("-")
    if index == 6 and len(temp) == 11:
        print("\nOK, perfekt personnummer är skrivit rätt.\n")
        break
    else:
        print("\nNEJ, det är inte rätt.\nEn gång till snälla")

# check av personnummer är rätt för skatteverket
# https://sv.wikipedia.org/wiki/Personnummer_i_Sverige

temp = temp.replace("-","")
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

# check för kön
# https://www.personnummer.nu/mer-information/

if int(temp[-2]) % 2 == 1:
    check_kön = input("Du är en man. Är det rätt? (S/N): ").lower()         
else:
    check_kön = input("Du är en kvinna. Är det rätt? (S/N): ").lower()


# global check

if check_sum == int(temp[-1]) and check_kön == "s":
    print("Personnummer är rätt för skatteverket\n")
else:
    print("Det finns en fel i ditt personnummer")
