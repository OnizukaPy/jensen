konsonanter = "bcdfghjklmnpqrstvwxz"

text = input("Skriv en text \n>: ").strip().lower()
text2 = ""

for i in text:
    for k in konsonanter:
        if i == k:
            i = (i+"o"+i)
    text2 += i

print(text2)