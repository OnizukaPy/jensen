# lete aefter det sista vita tecken i en text
text = input("Skriv en text här: \n> ")
c = 0
for i in range(len(text)):
    if text[i] == " " or text[i] == "\t":
        c = i

if c != 0:
    print(f"Den sista tecken finns på plats nr. {c}")
else:
    print("Inget vitt tecken")