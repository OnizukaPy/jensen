from nis import cat
from PIL import Image
from numpy import asarray
import os
import csv

class image:
    def __init__(self, path, filnamn):
        self.filnamn = filnamn                # path eller filnamn
        self.path = path
        self.pixel_värde = 0            # värden av imgs pixel summa 
        self.matrix = []
        self.vit = 0
        self.svart = 0

    def set_color(self):

        img = Image.open(self.path + self.filnamn)
        img = img.convert("L")
        img = img.resize((30,30))
        self.matrix = asarray(img)
        
        for i in range(0, 30):
            for j in range(0, 30):
                if self.matrix[i][j] >= 128:
                    self.vit += 1
                else:
                    self.svart += 1

        return (self.vit, self.svart)

path= "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
name_cat = "cat.0.jpg"
name_dog = "dog.10.jpg"

cat0 = image(path, name_cat)
print(name_cat, cat0.set_color())

dog0 = image(path, name_dog)
print(name_dog, dog0.set_color())