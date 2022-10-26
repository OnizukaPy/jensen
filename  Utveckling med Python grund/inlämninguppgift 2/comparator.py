import new as nw
import os
import numpy as np

path_train = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
list_train = os.listdir(path_train)

path_test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test2/"
list_test = os.listdir(path_test)

# lista delle immagini di catti e cani
train_list_cat = []
train_list_dog = []

for i in list_train:
    
    if "cat" in i:
        train_list_cat.append(i)
    elif "dog" in i:
        train_list_dog.append(i)

Kat = []
Dog = []
for i in train_list_cat:
    cat0 = nw.image(path_train, i)
    matrix =  cat0.show_matrix()
    Kat.append(matrix)

for i in train_list_dog:
    dog0 = nw.image(path_train, i)
    matrix =  dog0.show_matrix()
    Dog.append(matrix)

# lista delle immagini test
for namn in list_test:
    
    test_image = nw.image(path_test, namn)
    matrix =  test_image.show_matrix()

    # confronto

    dist_cat_list = []
    dist_dog_list = []

    for k in Kat:
        for i in range(30):
            for j in range(30):
                xt = float(matrix[i][j])
                xc = float(k[i][j])
                dist_cat = abs(xt - xc)
                dist_cat_list.append(dist_cat)

    for d in Dog:
        for i in range(30):
            for j in range(30):
                xt = float(matrix[i][j])
                xd = float(d[i][j])
                dist_dog = abs(xt - xd)
                dist_dog_list.append(dist_dog)

    #print(dist_cat_list)
    #print(dist_dog_list)

    # prediction
    accuracy = []
    cat_count = 0
    dog_count = 0

    for i in sorted(dist_cat_list)[0:3]:
        for j in sorted(dist_dog_list)[0:3]:
            if i < j:
                cat_count += 1
            else:
                dog_count += 1


    if cat_count > dog_count:
        print(namn, "cat")
        accuracy.append([namn, "cat"])
    elif dog_count > cat_count:
        print(namn, "dog")
        accuracy.append([namn, "dog"])
    else:
        print(namn, "x")
        accuracy.append([namn, "x"])

count = 0
for i in accuracy:
    if i[1] in i[0]:
        count += 1

print(f"{count/len(accuracy)*100:.2f}%")