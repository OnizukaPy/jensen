from PIL import Image
from numpy import asarray, seterr
from math import sqrt
import csv
seterr(over='ignore')

def getImg(imgPath, scaled_size):
    img = Image.open(imgPath)
    img = img.resize((scaled_size, scaled_size))
    img = img.convert('L')

    return img

def getDistance(Matrix1, Matrix2, scaled_size):

    diffSquared = 0
    for x in range (0, scaled_size):
        for y in range (0, scaled_size):
            
            diffSquared += round(( (Matrix1[x][y] - Matrix2[x][y]) ** 2 ),2)

    rms = round(sqrt(diffSquared), 2)

    return rms
class image:
    def __init__(self, imgPath, filnamn, scaled_size):

        self.filnamn = filnamn                
        self.imgPath = imgPath
        self.img = getImg(self.imgPath+self.filnamn, scaled_size)

    def getMatrix(self):

        self.matrix = asarray(self.img)

        return self.matrix

