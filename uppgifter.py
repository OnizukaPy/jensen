value_int = int(10)
value_string = "Python"
value_float = 12.43

while True:
    value_in = int(input("Kunde du skriva ett tal? "))
    if value_in > 0:
        print("Talet är positiv")
    elif value_in < 0:
        print("Talet är negativ")
    else:
        print("Det är lika 0")
    svar = input("Vill du fortsätta en gågn till s/n? ")
    if svar != "s":
        print("Hejdå")
        break
        
print("Fine")
