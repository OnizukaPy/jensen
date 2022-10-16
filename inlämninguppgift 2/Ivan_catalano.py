# https://savagerose.org/it/riconoscimento-di-immagini-in-python-con-tensorflow-e-keras/

# https://savagerose.org/it/riconoscimento-di-immagini-in-python-con-tensorflow-e-keras/
# https://www.rapidtables.com/web/color/RGB_Color.html

import funktioner as f
import matplotlib.pyplot as plt
import os

path = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train2/" 

# create list of filname of cats and dogs images 

list_train = os.listdir(path)

train_list_cat = []
train_list_dog = []

for i in list_train:
    
    if "cat" in i:
        train_list_cat.append(i)
    elif "dog" in i:
        train_list_dog.append(i)

# create a list of coordinater av cats images

punkt_list_cat = []
punkt_list_dog = []

for i in train_list_cat:

    cat0 = f.image(path, i)
    x, y = cat0.set_color()
    punkt_list_cat.append([cat0.filnamn, x, y])   # ["cat.0.jpg", x, y]

f.skriv_i_filen("Cat_list.csv", punkt_list_cat)

for i in train_list_dog:

    dog0 = f.image(path, i)
    x, y = dog0.set_color()
    punkt_list_dog.append([dog0.filnamn, x, y])   # ["dog.0.jpg", x, y]

f.skriv_i_filen("Dog_list.csv", punkt_list_dog)