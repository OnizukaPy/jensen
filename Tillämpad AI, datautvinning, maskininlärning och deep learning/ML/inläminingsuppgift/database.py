# importera moduler och bibliotek som behövs för att hantera mapper och filer
import os
import shutil

# importera moduler och bibliotek som behövs för att hantera data
import numpy as np
import pandas as pd

# importera moduler och bibliotek som behövs för att ladda ner data och förbehandla data
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

# importera modulen time för att skapa en paus mellan varje steg
import time 
sleep_time = 0.5

# skapa en mapp för att spara filen används path modulen
print("Skapar en mapp för att spara filen...\n")
PATH = os.path.dirname(os.path.abspath(__file__)) + "/"
time.sleep(sleep_time)
print(f"Mappen är skapad. Sökvägen är {PATH}\n")

# skapa en klass för att hantera databasen och skapa en dataframe
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
    
    # skapa en metod för att skriva ut en sammanfattning av datasetet
    def print_info(self):
        print("Skriver en sammanfattning av datasetet...\n")
        self.summary = (
            f"Dataset {self.filename} innebär bröstcancerdata.\n"
            f"Dataset är en {self.data_module}s module.\n"
            f"Dataset sammanfattning:\n\n"
            f"Antal rader: {self.data.shape[0]}\n"
            f"Antal kulumner: {self.data.shape[1]}\n"
            f"Antal klasser: {self.target_names.shape[0]}\n"
            f"Klassnamn: {self.target_names}\n"
        )
        return self.summary
    
    # skapa en metod för att skriva ut en beskrivning av datasetet
    def print_descr(self):
        return self.DESCR
    
    # skapa en metod för att spara sammanfattningen i en fil
    def save_info(self):
        print("Sparar sammanfattningen i en fil...\n")
        with open(PATH + "documents/"+"database.txt", "w") as f:
            f.write(self.summary + "\n" + self.DESCR)
            print("Sammanfattningen är sparad i filen database.txt")
            f.close()

    # skapa en metod för att skapa en dataframe från datasetet
    def create_dataframe(self):
        self.df = pd.DataFrame(
                        np.c_[self.data, self.target_names[self.target]],   # vi använder np.c_ för att lägga till target i data som objekt
                        columns = np.append(self.feature_names, ['target'])
                )
        return self.df
    
    # skapa en metod för att skala dataframe med StandardScaler
    def scale_dataframe(self):
        self.df_scaled = pd.DataFrame(StandardScaler().fit_transform(self.df.drop(['target'], axis = 1)), columns=self.df.columns[:-1])
        self.df = pd.concat([self.df_scaled, self.df['target']], axis = 1)

        return self.df

# skapa en funktion för att skapa mappar för att spara bilder och dokument
# om mapparna finns redan, tas de bort och skapas igen, används shutil modulen och os modulen
def create_directory():
    print("skapar mappen för att spara bilder...\n")
    try:
        # ta bort mappen om den finns
        if os.path.exists(PATH + "images"):
            print("Mappen images finns redan.\n")
            shutil.rmtree(PATH + "images")
            print("Mappen images är borttagen.\n")
            time.sleep(sleep_time)
            print("Skapar mappen images igen...\n")
            os.mkdir(PATH + "images")
            os.mkdir(PATH + "images/EDA")
            os.mkdir(PATH + "images/database")
            print("Mappen images är skapat.\n")
        else:
            os.mkdir(PATH + "images")
            os.mkdir(PATH + "images/EDA")
            os.mkdir(PATH + "images/database")
            print("Mappen images är skapat.\n")

        if os.path.exists(PATH + "documents"):
            print("Mappen documents finns redan.\n")
            shutil.rmtree(PATH + "documents")
            print("Mappen documents är borttagen.\n")
            time.sleep(sleep_time)
            print("Skapar mappen documents igen...\n")
            os.mkdir(PATH + "documents")
            print("Mappen documents är skapat.\n")
        else:
            os.mkdir(PATH + "documents")
            print("Mappen documents är skapat.\n")
        
        time.sleep(sleep_time)
        return "Mapparna är skapade.\n"

    except OSError:
        print("Error: Creating directory.\n")
        
# den här funktionen används för att initiera en databaset och skapa en sammanfattning av datasetet
def set_db():
    db = Database()
    print(db.print_info())
    db.save_info()

    return db

# den här funktionen används för att skapa en dataframe från datasetet och skala den
def set_df(db):

    df = db.create_dataframe()
    df = db.scale_dataframe()
    
    return df


