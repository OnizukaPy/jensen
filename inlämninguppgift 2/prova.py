import new as nw
import matplotlib.pyplot as plt
import os
import numpy as np

path_test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test2/"
list_test = os.listdir(path_test)

#print(list_test)

path_train = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
list_train = os.listdir(path_train)

train_list_cat = []
train_list_dog = []

for i in list_train:
    
    if "cat" in i:
        train_list_cat.append([path_train, i])
    elif "dog" in i:
        train_list_dog.append([path_train, i])

"""print("\n")
print(train_list_cat)
print("\n")
print(train_list_dog)
print("\n")"""

print("\n")

for namn in list_test:
    knn = 0
    dist_cat = []
    dist_dog = []
    
    test_image = nw.image(path_test, namn, 30)
    matrix =  test_image.getMatrix()
    
    
    for j in train_list_cat:
        path = j[0]
        name = j[1]
        img2 = nw.image(path, name, 30)
        d = nw.getDistance(matrix, img2.getMatrix(), 30)
        #print([d, name])
        dist_cat.append([d, name])

    for j in train_list_dog:
        path = j[0]
        name = j[1]
        img2 = nw.image(path, name, 30)
        d = nw.getDistance(matrix, img2.getMatrix(), 30)
        #print([d, name])
        dist_dog.append([d, name])
    
    knn = sorted(dist_cat + dist_dog)
    count = 0
    k = 15
    for i in range(0, k):
        if "cat" in knn[i][1]:
            count += 1
    print(f"{namn} kunde vara {count/len(knn[:k])*100:.0f}% en Kat och {(len(knn[:k])-count)/len(knn[:k])*100:.0f}% en Hund")
    #print(namn ,knn[:2])
    
    
  