import math
from os import listdir
from os.path import isfile, join
from PIL import Image
import random


##################################### Constants
K = 3 # How many nearest neighbors to use for classification
SCALED_SIZE = 32 # Number of X and Y pixels to scale images to
NUM_TEST_SAMPLES_PER = 10 # Number of test images to set aside for each class
DATA_PATH = "/home/onizuka-host/Scaricati/material/dogs-vs-cats/train/"
DOG_LABEL = 'dog'
CAT_LABEL = 'cat'

##################################### Main
def main():
    # Read Data
    data = {DOG_LABEL: [], CAT_LABEL: []}
    imgFiles = [f for f in listdir(DATA_PATH) if isfile(join(DATA_PATH, f))]
    print(imgFiles)
    for imgFile in imgFiles:
        imgFile = DATA_PATH + imgFile
        if CAT_LABEL in imgFile:
            print(imgFile, CAT_LABEL in imgFile)
            data[CAT_LABEL].append(imgFile)
            print(data[CAT_LABEL])
        elif DOG_LABEL in imgFile:
            print(imgFile, CAT_LABEL in imgFile)
            data[DOG_LABEL].append(imgFile)
            print(data[DOG_LABEL])
    print(len(data[DOG_LABEL]))


    # Split data
    testData = {CAT_LABEL: [], DOG_LABEL: []}
    random.shuffle(data[CAT_LABEL])
    random.shuffle(data[DOG_LABEL])
    for i in range(NUM_TEST_SAMPLES_PER):
        testData[CAT_LABEL].append(data[CAT_LABEL].pop(0))
        testData[DOG_LABEL].append(data[DOG_LABEL].pop(0))

    # Test
    correctCount = {DOG_LABEL: 0, CAT_LABEL: 0}
    for catTest in testData[CAT_LABEL]:
        print ("catTest", catTest)
        nearestNeighbors = knn(catTest, data)
        print ("nearestNeighbors", nearestNeighbors)
        prediction = max(set(nearestNeighbors), key=nearestNeighbors.count)
        print ("prediction", prediction)
        if prediction == CAT_LABEL:
            correctCount[CAT_LABEL] += 1
        print ("*"*20)
    for dogTest in testData[DOG_LABEL]:
        print ("dogTest", dogTest)
        nearestNeighbors = knn(dogTest, data)
        print ("nearestNeighbors", nearestNeighbors)
        prediction = max(set(nearestNeighbors), key=nearestNeighbors.count)
        print ("prediction", prediction)
        if prediction == DOG_LABEL:
            correctCount[DOG_LABEL] += 1
        print ("*"*20)

    # Print results
    print ("Correct dog predictions", correctCount[DOG_LABEL])
    print ("Dog prediction accuracy", correctCount[DOG_LABEL]/NUM_TEST_SAMPLES_PER)
    print ("Correct cat predictions", correctCount[CAT_LABEL])
    print ("Cat prediction accuracy", correctCount[CAT_LABEL]/NUM_TEST_SAMPLES_PER)

##################################### Functions
# Get nearest neighbor using KNN
def knn(testPoint, data):
    nearestDistance = [99999]*K
    nearestNeighbor = ["UNDEF"]*K
    dataNum = 0
    for key in data: # Loop through each label
        for point in data[key]: # Loop through each data point
            dataNum += 1
            # Calcaulte distance and check if it is nearest
            distance = getDistance(testPoint, point)
            ## print ("Distance", distance)
            if distance < nearestDistance[0]: # Replace
                nearestDistance[0] = distance
                nearestNeighbor[0] = key
                # Sort
                zippedData = zip(nearestDistance, nearestNeighbor)
                sortedPairs = sorted(zippedData, reverse=True)
                tuples = zip(*sortedPairs)
                nearestDistance, nearestNeighbor = [ list(tuple) for tuple in  tuples]
                ###print ("nearestNeighbor", nearestNeighbor, "nearestDistance", nearestDistance, "dataNum", dataNum)
    return nearestNeighbor

# Calculates distance between tuples
def getDistance(img1Path, img2Path):
    img1 = getImg(img1Path)
    img2 = getImg(img2Path)
    diffSquared = 0
    for x in range (0, SCALED_SIZE):
        for y in range (0, SCALED_SIZE):
            cord = x, y
            diffSquared += ( (img1.getpixel(cord) - img2.getpixel(cord)) ** 2 )
    rms = math.sqrt(diffSquared)
    return rms

# Gets image and converts to a scaled black and white image
def getImg(imgPath):
    img = Image.open(imgPath)
    img = img.resize( (SCALED_SIZE, SCALED_SIZE) )
    img = img.convert('L')
    return img

if __name__ == "__main__":
    main()

