from PIL import Image
from numpy import asarray
from math import sqrt

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
        img = img.resize((100,100))
        self.matrix = asarray(img)
        
        for i in range(0, 100):
            for j in range(0, 100):
                if self.matrix[i][j] >= 192:
                    self.vit += 1
                elif self.matrix[i][j] <= 64:
                    self.svart += 1

        return self.vit, self.svart

    def show_matrix(self):

        img = Image.open(self.path + self.filnamn)
        img = img.convert("L")
        img = img.resize((30,30))
        self.matrix = asarray(img)

        return self.matrix

def avstånd_punkt(a, b):

    x1 = a[0]
    y1 = a[1]
    x2 = b[0]
    y2 = b[1]

    dist = sqrt((x2-x1)**2 + (y2 - y1)**2)

    return round(dist, 2)

def skriv_i_filen(namn, list):

    with open(namn, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in list:
            spamwriter.writerow(i)

def läs_från_filen(namn):
    temp = []
    with open(namn, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",")
        for row in spamreader:
            temp.append(row)

    return temp