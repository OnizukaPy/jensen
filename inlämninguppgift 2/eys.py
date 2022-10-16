from PIL import Image
from numpy import asarray
import csv
import pprint

def skriv_i_filen(namn, list):

    with open(namn, 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile)
        for i in list:
            spamwriter.writerow(i)

path = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
name = "cat.9465.jpg"
img = Image.open(path+name)
img = img.convert("L")
img = img.resize((40,40))
numpydata = asarray(img)

for i in range(40):
    for j in range(40):
        if numpydata[i][j] > 128:
            numpydata[i][j] = 0

for i in range(len(numpydata)):
    print(numpydata[i])
#print(numpydata)
#skriv_i_filen("eye.csv", numpydata)

# definire quanti pixel bianchi e neri ci sono in una immagine prendendo a riferimento poche immagini campione
# ogni immagine sarä poi definita da un punto avente x = bianco y =  nero