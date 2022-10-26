
text = input("Skriv en text på svenska\n>: ").strip().lower()
text2 = text
j = ""
for i in text:
    if i == "å":
        text2 = text2.replace("å", "aa")
    elif i == "ä":
        text2 = text2.replace("ä", "ae")
    elif i == "ö":
        text2 = text2.replace("ö", "oe")
    
print(text2)

temp = text2
print(len(text2))
for i in range(len(text2)):

    if (text2[i-1]+text2[i]) == "aa":
        temp = temp.replace("aa", "å")
        #print(temp)
    elif (text2[i-1]+text2[i]) == "ae":
        temp = temp.replace("ae", "ä")
        #print(temp)
    elif (text2[i-1]+text2[i]) == "oe":
        temp = temp.replace("oe", "ö")
        #print(temp)
    else:
        continue

print(temp)