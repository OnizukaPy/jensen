# Skriv err program som läser in en mening, bestående av minst två ord
# Programmet ska sedan visa ett meddelande där det dels talar om hur många tecken användaren skrev
# och dels talar om vilket som var det första resp. det sista ordet.
check = 0
while True:
    
    text = input("Skriv en mening: \n> ")
    temp = text.strip().lower()
    for t in temp:
        if t == " " or t == "\t":
            check = 1
    if check == 1:
        print("\nOk, mening bestående minst av två ord\n")
        check = 0
        break
    else:
        print("\nNEJ, mening bestående inte minst av två ord.\nEn gång till snälla.\n")

print("Programmet börjar..\n")
count_tecken = len(text)
print(f"1 - Användaren har skrivit {count_tecken} tecken\n")
# för att veta när slutar första ord vi kan använda funktion find()

index_f = temp.find(" ")
index_s = temp.rfind(" ")
första_ord = temp[:index_f+1]
sista_ord = temp[index_s+1:]

print(f"2 - Första ord är: {första_ord} och sita ord är: {sista_ord}\n")
print("\nProgrammet slutit. Goodbye!\n")
