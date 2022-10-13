from PIL import Image
from numpy import asarray
import os
import csv

def ränka_pixel(path):

    img = Image.open(path)
    img = img.convert("L")
    img = img.resize((30,30))
    numpydata = asarray(img)

    cat_1 = 0
    for i in range(0, 30):
        for j in range(0, 30):
            cat_1 += numpydata[i,j] 
    #print(cat_1)

    return cat_1


path = "inlämninguppgift 2/dogs-vs-cats/train/"
dir_list = os.listdir(path)

cat = []
dog = []
#print(dir_list)
for n in dir_list:
    #print(n)
    if "cat" in n:

        cat_1 = ränka_pixel(path + n)
        cat.append(cat_1)

    elif "dog" in n:

        dog_1 = ränka_pixel(path + n)
        dog.append(dog_1)

cat_value = (sum(cat)/len(cat))
dog_value = (sum(dog)/len(dog))

result = []

with open('result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for n in dir_list:
        value = ränka_pixel(path + n)
        if value >= dog_value: 
            spamwriter.writerow([n, "DOG"])
            result.append([n, "DOG"])
        elif value <= cat_value:
            spamwriter.writerow([n, "CAT"])
            result.append([n, "CAT"])
        else:
            if (dog_value - value) > (value - cat_value):
                spamwriter.writerow([n, "CAT"])
                result.append([n, "CAT"])
            else:
                spamwriter.writerow([n, "DOG"])
                result.append([n, "DOG"])
summa = 0
for i in range(len(result)):
    if result[i][1].lower() in result[i][0]:
        summa += 1

print(f"accuracy {summa/len(result)*100:.2f}")
      

#path_2 = "inlämninguppgift 2/dogs-vs-cats/test1/"
##
#while True:
#    test = input("Skriv namnet av filen som du vill testa: ")
#    if test in dir_list:
#        value = ränka_pixel(path + test)
#        if value > dog_value: 
#            print(f"Det här är en CAT och du har skrivit {test}")
#        elif value < cat_value:
#            print(f"Det här är en DOG och du har skrivit {test}")
#        else:
#            if (dog_value - value) > (value - cat_value):
#                print(f"Det här är en DOG och du har skrivit {test}")
#            else:
#                print(f"Det här är en CAT och du har skrivit {test}")
#            
#        check = input("\nVill du göra det en gång till? S/N: ").upper()
#        if check != "S":
#            break
#    else:
#        print("Filen är inte i directory, en gång till")

