import funktioner as f
import matplotlib.pyplot as plt
import os
import numpy as np

test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test2/"
list_test = os.listdir(test)

accuracy = []
for namn in list_test:
    
    test_image = f.image(test, namn)
    x, y =  test_image.set_color2()
    plt.plot(x, y, color="y", marker="o")

    Kat = f.läs_från_filen("inlämninguppgift 2/Cat_list.csv")
    Dog = f.läs_från_filen("inlämninguppgift 2/Dog_list.csv")

    dist_cat_list = []
    dist_dog_list = []
    for i in range(len(Kat)):
        xc = Kat[i][1]
        yc = Kat[i][2]
        dist_cat = f.avstånd_punkt([x, y], [xc, yc])
        dist_cat_list.append(dist_cat)
        

    for i in range(len(Dog)):
        xd = Dog[i][1]
        yd = Dog[i][2]
        dist_dog = f.avstånd_punkt([x, y], [xd, yd])
        dist_dog_list.append(dist_dog)
        

    cat_count = 0
    dog_count = 0

    for i in sorted(dist_cat_list)[0:2]:
        for j in sorted(dist_dog_list)[0:2]:
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
# Plotting

for i in Kat:
    plt.plot(float(i[1]), float(i[2]), color="r", marker="o")

for i in Dog:
    plt.plot(float(i[1]), float(i[2]), color="g", marker="o")

#plt.plot(coord[0], coord[1], color="yellow", marker="p")

plt.show()