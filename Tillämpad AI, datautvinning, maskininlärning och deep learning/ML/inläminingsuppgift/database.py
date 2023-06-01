import os

import numpy as np
import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

import time 
sleep_time = 0.5

# skapa en mapp för att spara filen
print("Skapar en mapp för att spara filen...\n")
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
time.sleep(sleep_time)
print(f"Mappen är skapad. Sökvägen är {PATH}\n")

class Database:
    def __init__(self):
        self.db = load_breast_cancer()
        self.data = self.db['data']
        self.target = self.db['target']
        self.feature_names = self.db['feature_names']
        self.target_names = self.db['target_names']
        self.filename = self.db['filename']
        self.data_module = self.db['data_module']
        self.DESCR = self.db['DESCR']
    
    def print_info(self):
        self.summary = (f"Database summary:\n\n"
            f"Number of samples: {self.data.shape[0]}\n"
            f"Number of features: {self.data.shape[1]}\n"
            f"Number of classes: {self.target_names.shape[0]}\n"
            f"Class names: {self.target_names}\n"
        )
        return self.summary
    
    def print_descr(self):
        return self.DESCR
    
    def save_info(self):

        with open(PATH+"database.txt", "w") as f:
            f.write(self.summary + "\n" + self.DESCR)
            print("Sammanfattningen är sparad i filen database.txt")
            f.close()

    def create_dataframe(self):
        self.df = pd.DataFrame(
                        np.c_[self.data, self.target_names[self.target]], 
                        columns = np.append(self.feature_names, ['target'])
                )
        return self.df
    
    def scale_dataframe(self):
        self.df_scaled = pd.DataFrame(StandardScaler().fit_transform(self.df.drop(['target'], axis = 1)), columns=self.df.columns[:-1])
        self.df = pd.concat([self.df_scaled, self.df['target']], axis = 1)

        return self.df



# ladda in datasetet
print("\nLaddar in datasetet...\n")
db = Database()
time.sleep(sleep_time)
print("Datasetet är laddat.\n")
time.sleep(sleep_time)
print("Skriver en sammanfattning av datasetet...\n")
print(db.print_info())
time.sleep(sleep_time)

print("Skriver en deskrition.\n")
print(db.print_descr())
time.sleep(sleep_time)

print("Sparar sammanfattningen i en fil...\n")
db.save_info()
time.sleep(sleep_time)

print("Skapar en dataframe...\n")
df = db.create_dataframe()

print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")
time.sleep(sleep_time)

print("Skalar dataframe...\n")
df = db.scale_dataframe()

print(df.head(), "\n")
print(df.info(), "\n")
print(df.describe(), "\n")





time.sleep(sleep_time)
print("Datasetet är laddat.\n")


