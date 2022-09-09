årkort = int(input("skriv priset av årkortet: "))
biljett = int(input("skriv priset av ett enkelt biljett: "))
gånger = int(input("hur många gånger vill du besöka gymmet?: "))

if (gånger * biljett) < årkort:
    print("Det är billigare att du köpa biljetter")
else:
    print("Det är billigare att du köpa årkort")

print(f"Du kan besöka gymmet bara {int(årkort/biljett)} gånger om du vill spara pengar")