while True:

    text = input("Skriv ditt e-postadress: ").strip().lower()

    if text.find("@") != -1:
        c = text.split("@")
        if c[0].find(".") != -1 and c[1].find(".") != -1:
            print("\nok du har skrivit korrekt")
            b = c[0].split(".")
            #d = c[1].split(".")
            print(f"\nHej {b[0]} {b[1]}, ditt domain är {c[1]}")
            break
    else:
        print("\nNej, du måste skriva korrekt")


