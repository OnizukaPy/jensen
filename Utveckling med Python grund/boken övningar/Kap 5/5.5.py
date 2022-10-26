text = input("Skriv en rövarspråk text: \n> ").strip().lower()
temp = text
for i in range(len(text)):
    if text[i-2] == text[i] and text[i-1] == "o":
        #print(text[i-2], text[i-1], text[i])
        j = text[i-2] + text[i-1] + text[i]
        k = text[i-2]
        #print(j, k)
        temp = temp.replace(j, k)
    else:
        continue
print(temp)