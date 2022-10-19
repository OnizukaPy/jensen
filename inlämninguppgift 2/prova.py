import new as nw
import matplotlib.pyplot as plt
import os
import numpy as np

test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test2/"
list_test = os.listdir(test)

accuracy = []
for namn in list_test:
    
    test_image = nw.image(test, namn)
    matrix =  test_image.show_matrix()
    
    Kat = nw.läs_från_filen("inlämninguppgift 2/Cat_list.csv")
    Dog = nw.läs_från_filen("inlämninguppgift 2/Dog_list.csv")

    print(Kat[1])

    dist_cat_list = []
    dist_dog_list = []
    for k in Kat:
        for i in range(30):
            for j in range(30):
                xt = matrix[i][j]
                xc = k[1][i][j]
                dist_cat = abs(xt - xc)
                dist_cat_list.append(dist_cat)

    for d in Dog:
        for i in range(30):
            for j in range(30):
                xt = matrix[i][j]
                xd = d[1][i][j]
                dist_dog = abs(xt - xd)
                dist_dog_list.append(dist_dog)

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