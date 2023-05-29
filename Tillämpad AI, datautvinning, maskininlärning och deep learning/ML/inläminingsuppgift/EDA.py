# importera en dataset från sklearn
# vi väljer att importera breast cancer dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer

import os

# skapa en mapp för att spara filen
path = os.path.dirname(os.path.abspath(__file__)) + "/"

# ladda in datasetet
cancer = load_breast_cancer()

förts_välj = input("Vill du se en deskrion av datasetet? (j/n): ")
if förts_välj.lower() == "j":

    # skriva en sammanfattning av datasetet
    sammanfatning = (
        f"Databasen innehåller information om bröstcancer.\n\n"
            f"Database filename är {cancer['filename']}\n"
            f"Vi importerar databasen från den {cancer['data_module']} module\n\n"
        f"Database summary:\n"
            f"Number of samples: {cancer['data'].shape[0]}\n"
            f"Number of features: {cancer['data'].shape[1]}\n"
            f"Number of classes: {cancer['target_names'].shape[0]}\n"
            f"Number of missing values: {np.isnan(cancer['data']).sum()}\n"
            f"Number of unique values: {np.unique(cancer['data']).shape[0]}\n"
            f"Number of features with missing values: {np.isnan(cancer['data']).any().sum()}\n"
            f"Number of features with constant values: {np.unique(cancer['data'], axis=0).shape[0]}\n"
            f"Number of features with duplicated values: {cancer['data'].shape[1] - np.unique(cancer['data'], axis=1).shape[1]}\n"
            f"Number of features with zero values: {np.count_nonzero(cancer['data'] == 0)}\n"
    ) + "\n" + (cancer['DESCR'])
    print(sammanfatning)
    # sparar sammanfattningen i en fil
    with open(path+"database.txt", "w") as f:
        f.write(sammanfatning)
        print("Sammanfattningen är sparad i filen database.txt")
        f.close()

else:
    print("Okej, vi går vidare till nästa steg.")

