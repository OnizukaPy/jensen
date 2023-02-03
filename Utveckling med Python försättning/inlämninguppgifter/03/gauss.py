# Title: Gausselimination pch andra funktioner
# importera numpy
import numpy as np

## ------------------ Funktions script  ------------------ ##
## Funktioner

# utbytta rader
def utbyta_rader(m, a, b):
    """
    Byter plats på raderna a och b i matrisen m
    """
    temp = m[a].copy()
    m[a] = m[b]
    m[b] = temp
    return m

# ordna matriser
def ordna_matris(a, b):
    """
    Ordna matriser: 
    a är matrisen
    b är vektoren  
    """
    n = len(a)
    for i in range(n):
        if a[i, 0] == 0:
            utbyta_rader(a, i, n-1)
            utbyta_rader(b, i, n-1)

    return a, b

# Gausselimination
def gauss_elimination(a, b):
    """
    Gausselimination: 
    a är matrisen av koefficenterna 
    b är vektorerna av konstanterna
    """
    ordna_matris(a, b)
    n = len(b)
    j = 0
    while j < 2:
        for i in range(j, n-1):
            k = (a[i+1, j] / a[j, j])
            a[i+1] = k * a[j] - a[i+1]
            b[i+1] = k * b[j] - b[i+1]

        j += 1

    return a, b

# hitta lösningarna med Gausselimination
def solve_gauss(a, b):
    """
    Hitta lösningarna med Gausselimination metoden
    a är matrisen av koefficenterna
    b är vektorerna av konstanterna
    returnerar vektorn x med lösningarna
    """
    gauss_elimination(a, b)
    n=len(b)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        #print('i+1:n:', f'{i+1}:{n}')
        #print('a[i, i+1:n]:', a[i, i+1:n])
        #print('x[i+1:n]:', x[i+1:n])
        x[i] = (b[i] - np.dot(a[i, i+1:n], x[i+1:n]))/a[i, i]

    return x

# Skapa matriser för Gausselimination
def skapa_norekv_from_df(df, column_name):
    """
    Skapa den normala ekvationer för att använda Gausselimination
    df är databasen som ska användas
    column_name är kolumnen som ska användas
    """

    x = range(len(df))
    y = df[column_name]
    a = []
    for i in range(0, len(x)):
        a.append(x[i])
        a.append(1)

    A = np.array(a,dtype=float)
    A = A.reshape(len(x), 2)
    Y = np.array(y,dtype=float)

    At = A.transpose()
    A = np.dot(At, A)
    Y = np.dot(At, Y)

    return A, Y

# Skriv ut ekvationen
def skriv_ekvation(x_values):
    """
    skriv ut ekvationen med koefficenterna
    """

    k = round(x_values[0], 2)
    m = round(x_values[1], 2)
    if (m<0):
        print(f'y={k}x{m}')
    else:
        print(f'y={k}x+{m}')
    
    return k, m


## ------------------ Funktions script  ------------------ ##