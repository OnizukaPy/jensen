import funktioner as f
import matplotlib.pyplot as plt
import os



test = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/test2/"
list_test = os.listdir(test)

for namn in list_test:
    test_image = f.image(test, namn)
    coord =  test_image.set_color()

    #print(f"\ncoordinaterna: ({coord[0]}, {coord[0]})\n")

    Kat = f.läs_från_filen("Cat_list.csv")
    Dog = f.läs_från_filen("Dog_list.csv")

    dist_cat_list = []
    dist_dog_list = []
    for i in range(len(Kat)):
        xc = int(Kat[i][1])
        yc = int(Kat[i][2])
        dist_cat = f.avstånd_punkt(coord, [xc, yc])
        dist_cat_list.append(dist_cat)

    for i in range(len(Dog)):
        xd = int(Dog[i][1])
        yd = int(Dog[i][2])
        dist_dog = f.avstånd_punkt(coord, [xd, yd])
        dist_dog_list.append(dist_dog)

    cat_count = 0
    dog_count = 0

    #print(sorted(dist_cat_list))
    #print(sorted(dist_dog_list))

    for i in sorted(dist_cat_list)[0:2]:
        for j in sorted(dist_dog_list)[0:2]:
            if i < j:
                cat_count += 1
            else:
                dog_count += 1


    if cat_count > dog_count:
        print(namn, "KAT")
    elif dog_count > cat_count:
        print(namn, "DOG")
    else:
        print(namn, "VET INTE")

# Plotting

#for i in Kat:
#    plt.plot(int(i[1]),int(i[2]), color="red", marker="o")

#for i in Dog:
#    plt.plot(int(i[1]),int(i[2]), color="green", marker="o")

#plt.plot(coord[0], coord[1], color="yellow", marker="p")

#plt.show()