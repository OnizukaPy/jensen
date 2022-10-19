from PIL import Image
from numpy import asarray
from math import sqrt
import csv

class image:
    def __init__(self, path, filnamn):
        self.filnamn = filnamn                # path eller filnamn
        self.path = path
        self.matrix = []

    def show_matrix(self):

        img = Image.open(self.path + self.filnamn)
        img = img.convert("L")
        img = img.resize((30,30))
        self.matrix = asarray(img)

        return self.matrix

def avstånd_punkt(a, b):

    dist = sqrt((a-b)**2)

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