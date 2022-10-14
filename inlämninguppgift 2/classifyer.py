import csv

test_list_img_data = []
with open('/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/inlämninguppgift 2/test.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        test_list_img_data.append(row)

train_list_cat = []
train_list_dog = []
with open('/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/inlämninguppgift 2/cat.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        train_list_cat.append(row)

with open('/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/inlämninguppgift 2/cat.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=",")
    for row in spamreader:
        train_list_dog.append(row)

print(len(test_list_img_data))
print("\n")
print(len(train_list_cat))
print("\n")
print(len(train_list_dog))
print("\n")

cat = 0
dog = 0
na = 0
result = []
with open('/home/onizuka-host/Zoho WorkDrive (Catalano Consulenze Tecniche)/My Folders/Documenti personali_/Corsi/Scuola di Python con Jensen/Esercizi/jensen/inlämninguppgift 2/result.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    
    for i in train_list_cat:
        for j in range(len(train_list_cat)):
            if i[2] <= train_list_cat[j][2]:
                cat += 1
            elif i[1] >= train_list_dog[j][2]:
                dog += 1
            elif i[1] < train_list_dog[j][2] and i[1] > train_list_cat[j][2]:
                if abs(i[1] - train_list_dog[j][2]) > abs(i[1] - train_list_cat[j][2]):
                    cat += 1
                elif abs(i[1] - train_list_dog[j][2]) < abs(i[1] - train_list_cat[j][2]):
                    dog += 1
                else:
                    na += 1
            else:
                na += 1
        if cat > dog:
            vin = "CAT"
        elif dog > cat:
            vin ="DOG"
        else:
            vin = "VET INTE"
        result.append([i[0], cat, dog, na, cat/(cat+dog+na)*100, dog/(cat+dog+na)*100, vin])
        spamwriter.writerow([i[0], cat, dog, na, vin, f"det är {cat/(cat+dog+na)*100:.2f}% en kat och {dog/(cat+dog+na)*100:.2f}% en hund"])
        cat = 0
        dog = 0
        na = 0

print(result)




path_train = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
path_test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test1/"
list_train = os.listdir(path_train)
list_test = os.listdir(path_test)

test_list_img_data = []
with open('test.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in list_test:
        m = image(path_test, i)
        pixel = m.ränka_pixel_värde()
        test_list_img_data.append([m.filnamn, pixel])
        spamwriter.writerow([m.filnamn, pixel])



print("\n")
print(test_list_img_data)
print("\n")
train_list_cat = []
train_list_dog = []

for i in list_train:
    m = image(path_train, i)
    
    if "cat" in i:
        pixel = m.ränka_pixel_värde()
        train_list_cat.append(["CAT", m.filnamn, pixel])   
    else:
        pixel = m.ränka_pixel_värde()
        train_list_dog.append(["DOG", m.filnamn, pixel])        

with open('cat.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in train_list_cat:
        spamwriter.writerow(i)

with open('dog.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile)
    for i in train_list_dog:
        spamwriter.writerow(i)

print(train_list_cat)
print("\n")
print(train_list_dog)
print("\n")

