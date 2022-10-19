from PIL import Image

import numpy as np
import csv
import pprint

def skriv_i_filen(namn, list):

    with open(namn, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in list:
            spamwriter.writerow(i)

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

path = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
name = "cat.1.jpg"
img = Image.open(path+name)
img = img.convert("L")
img = img.resize((30,30))
#img.show()

numpydata = np.asarray(img)

kernel = np.array([  [1, 0, -1], 
                [1, 0, -1], 
                [1, 0, -1]])


#print("\nimg1\n")
#for i in range(len(numpydata)):
#    print(numpydata[i])

vit = 1
svart = 1
for i in range(0, 30):
    for j in range(0, 30):
        if numpydata[i][j] >= 128:
            vit += 1
        else:
            svart += 1

s_v = round(vit/svart, 2)*100
cnn_v = cnn(numpydata, kernel)

print(s_v, cnn_v)
#for i in range(len(numpydata)):
#    print(numpydata[i])

#img2 = Image.fromarray(numpydata)
#img2.show()

#print("\nimg2\n")
#for i in range(len(numpydata)):
#    print(numpydata[i])
#print(numpydata)
#skriv_i_filen("eye.csv", numpydata)

# definire quanti pixel bianchi e neri ci sono in una immagine prendendo a riferimento poche immagini campione
# ogni immagine sarä poi definita da un punto avente x = bianco y =  nero

# prendere una immagine campione del gatto e del cane e convertirla nel punto bianco e nero.
# traslare l+immagine del gatto sull+asse x e quella del cane sull+asse y e usare questo punto come punto
#per traslare tutti gli altri