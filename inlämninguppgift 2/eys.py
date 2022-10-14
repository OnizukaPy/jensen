from PIL import Image
from numpy import asarray

path = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/" 
name = "cat.9465.jpg"
img = Image.open(path+name)
img = img.convert("L")
img = img.resize((8,8))
numpydata = asarray(img)

print(numpydata)

# definire quanti pixel bianchi e neri ci sono in una immagine prendendo a riferimento poche immagini campione
# ogni immagine sarä poi definita da un punto avente x = bianco y =  nero