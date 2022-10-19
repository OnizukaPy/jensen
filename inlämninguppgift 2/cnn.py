import numpy as np

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
    k = len(x)-len(y)+1
    a = np.array(result).reshape((k, k))

    return a

x = np.array([  [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 6],
                [3, 4, 5, 6, 7],
                [4, 5, 6, 7, 8],
                [5, 6, 7, 8, 9]])

#print(x[0])

y = np.array([  [1, 0, -1], 
                [1, 0, -1], 
                [1, 0, -1]])


new =[]
for i in range(len(x)):
    for j in range(len(x[i])-2):
        new.append([x[i][j], x[i][j+1], x[i][j+2]])

mat = []
#count = 1
for i in range(0, len(new)-6):
    #print(count)
    #print(i, i+3, i+6)
    mat.append([new[i], new[i+3], new[i+6]])
    #count += 1
#print(len(mat))

temp = 0
result = []
for i in range(len(mat)):
    #print("\n", i, "\n")
    for j in range(len(y)):
        for k in range(len(y)):
            temp += mat[i][j][k]*y[j][k]
            #print(mat[i][j][k], y[j][k], temp)
        
    result.append(temp)
    temp = 0
#print(result)

a = sum(result)

print(a)

print(cnn(x, y))