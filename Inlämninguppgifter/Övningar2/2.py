vokaler = "aeiouyåäö"
ok = True
while ok:
    text = input("Skriv ett ord på svenska: ").strip().lower()
    check = len(text)
    for v in text:
        if v not in vokaler:
            check += -1
            #print(check)
    
    if check > 0:

        for v in text:
            if v in vokaler:
                index = text.find(v)+1
                print(f"\nJag har hittat den första vokalen: {v}, i platsen {index}")
                ord1 = text[:index]
                ord2 = text[index:]
                new_ord2 = "fi"+ord2
                new_ord1 = ord1+"kon"
                print(ord1, ord2, ("fi"+ord2+" "+ord1+"kon"))
                break
        
        check2 = input("Vill du fortsätta? (s/n): ").strip().lower()
        if check2 != "s": 
            ok = False

    else:
        print("\nDu har skrivit ett ord utan vokaler")






