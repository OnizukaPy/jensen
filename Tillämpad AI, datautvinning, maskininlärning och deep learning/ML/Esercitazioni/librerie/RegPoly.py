import numpy as np
import warnings
warnings.filterwarnings('ignore')
from sklearn.metrics import r2_score

# creiamo una classe per il regressore polinomiale

class Rgpoly:

    def __init__(self, degree):
        self.degree = degree

    # il metodo fit calcola i coefficienti del polinomio e li salva in self.p la 
    # funzione polinomiale
    def fit(self, X, y):
        z = np.polyfit(X.flatten(), y.flatten(), self.degree)
        self.p = np.poly1d(z)
        
    # il metodo predict calcola il valore del polinomio per ogni valore di X
    def predict(self, X):
        return self.p(X)
    
def best_degree(X, y, d_min, d_max):

    error_list = []
    for i in range(d_min, d_max + 1):

        # creiamo un regressore polinomiale di grado i
        reg = Rgpoly(i)
        # calcoliamo i coefficienti del polinomio
        reg.fit(X, y)
        # calcoliamo il valore del polinomio per ogni valore di X
        y_poly = reg.predict(X)

        # calcoliamo le metriche
        r2 = r2_score(y, y_poly)

        # aggiungiamo i valori delle metriche alla lista
        error_list.append([i, r2])
    
    # calcoliamo il miglior valore di r2 e il suo indice nella lista
    r2_list = [i[1] for i in error_list]
    r2_max = max(r2_list)
    r2_max_index = r2_list.index(r2_max)

    # stampiamo il valore di r2 e l'ordine del polinomio
    best_r2 = r2_max
    best_degree = error_list[r2_max_index][0]

    return best_degree, best_r2
