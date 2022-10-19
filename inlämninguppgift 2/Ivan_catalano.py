# https://savagerose.org/it/riconoscimento-di-immagini-in-python-con-tensorflow-e-keras/

# https://savagerose.org/it/riconoscimento-di-immagini-in-python-con-tensorflow-e-keras/
# https://www.rapidtables.com/web/color/RGB_Color.html

import new as nw
import matplotlib.pyplot as plt
import os
import numpy as np


path = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
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
    print(i)
    cat0 = nw.image(path, i)
    matrix = cat0.show_matrix()
    punkt_list_cat.append([cat0.filnamn, matrix])  

nw.skriv_i_filen("inlämninguppgift 2/Cat_list.csv", punkt_list_cat)

for i in train_list_dog:
    print(i)
    dog0 = nw.image(path, i)
    matrix = dog0.show_matrix()
    punkt_list_dog.append([dog0.filnamn, matrix]) 

nw.skriv_i_filen("inlämninguppgift 2/Dog_list.csv", punkt_list_dog)