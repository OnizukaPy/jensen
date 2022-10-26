
while True:
    höjd = int(input("\nSkriv höjden: "))
    höjd_b = höjd
    i = 0
    if höjd <=0:
        print("\nFörlåt men höjden kan inte vara negativ. \nHejdå!\n")
        break
    else:
        while höjd > 0.01:

            #print(f"{i} gång. Höjden är {höjd:.2f}. ", end=" ")
            höjd *= 0.7
            i += 1
            #print(f"Nu är det {höjd:.2f} meter", end="\n")
        else:
            print(f"\nFrån {höjd_b:.2f} meter är ballen stilla på golvet efter {i} gånger")
            i = 0
            

        val = input("\nVill du forsätta? to quit pres n: ")
        if val == "n":
            print("\nHejdå!\n")
            break

    
    