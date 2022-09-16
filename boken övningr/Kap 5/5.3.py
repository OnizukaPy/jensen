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

personnummer_list = []
for i in text:
    personnummer_list.append(int(i))

summa = (sum(personnummer_list[0:len(personnummer_list)-1:2])*2 + sum(personnummer_list[1:len(personnummer_list):2]))
check_sum = (10 - (summa%10)) % 10
if check_sum == list[-1]:
    print("Personnummer är rätt för skatteverket\n")

# check för kön
# https://www.personnummer.nu/mer-information/

if personnummer_list[-2] % 2 == 0:
    print("Du är en kvinna!\nHejdå!\n")
else:
    print("Du är en man!\nHejdå!\n")