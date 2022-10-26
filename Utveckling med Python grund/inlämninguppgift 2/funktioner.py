from PIL import Image
from numpy import asarray
from math import sqrt

import csv

def cnn(x, y):
    new =[]
    mat = []
    temp = 0
    result = []
    for i in range(len(x)):
        for j in range(len(x[i])-2):
            new.append([x[i][j], x[i][j+1], x[i][j+2]])

    for i in range(0, len(new)-6):
        mat.append([new[i], new[i+3], new[i+6]])


    for i in range(len(mat)):
        for j in range(len(y)):
            for k in range(len(y)):
                temp += mat[i][j][k]*y[j][k]

        result.append(temp)
        temp = 0    
    
    a = sum(result)

    return a

class image:
    def __init__(self, path, filnamn):
        self.filnamn = filnamn                # path eller filnamn
        self.path = path
        self.pixel_värde = 0            # värden av imgs pixel summa 
        self.matrix = []
        self.vit = 1
        self.svart = 1

    def set_color(self):

        img = Image.open(self.path + self.filnamn)
        img = img.convert("L")
        img = img.resize((30,30))
        self.matrix = asarray(img)
        
        for i in range(0, 30):
            for j in range(0, 30):
                if self.matrix[i][j] >= 192:
                    self.vit += 1
                elif self.matrix[i][j] <= 64:
                    self.svart += 1

        return self.vit, self.svart
    
    def set_color2(self):

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

        return self.vit, self.svart    

    def set_color3(self, kernel):

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
        
        v_s = int(self.vit/self.svart*100)
        cnn_v = cnn(self.matrix, kernel)

        return  v_s, cnn_v

    def show_matrix(self):

        img = Image.open(self.path + self.filnamn)
        img = img.convert("L")
        img = img.resize((30,30))
        self.matrix = asarray(img)

        return self.matrix

def avstånd_punkt(a, b):

    x1 = float(a[0])
    y1 = float(a[1])
    x2 = float(b[0])
    y2 = float(b[1])

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

