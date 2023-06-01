# importera en dataset från sklearn
# vi väljer att importera breast cancer dataset

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_breast_cancer
from sklearn.preprocessing import StandardScaler

import os

# skapa en mapp för att spara filen
path = os.path.dirname(os.path.abspath(__file__)) + "/"

# ladda in datasetet
cancer = load_breast_cancer()
df_cancer = pd.DataFrame(
                    np.c_[cancer['data'], cancer['target']], 
                    columns = np.append(cancer['feature_names'], ['target'])
            )
scaler = StandardScaler()
df_cancer_scaled = pd.DataFrame(scaler.fit_transform(df_cancer.drop(['target'], axis = 1)), columns=df_cancer.columns[:-1])

df_cancer = pd.concat([df_cancer_scaled, df_cancer['target']], axis = 1)

förts_välj = input("Vill du se en deskrion av datasetet? (j/n): ")
if förts_välj.lower() == "j":

    # skriva en sammanfattning av datasetet
    sammanfatning = (
        f"\n\nDatabasen {cancer['filename']} innehåller information om bröstcancer. Vi importerar databasen från den {cancer['data_module']} module.\n\n"
        f"Database summary:\n\n"
            f"Number of samples: {cancer['data'].shape[0]}\n"
            f"Number of features: {cancer['data'].shape[1]}\n"
            f"Number of classes: {cancer['target_names'].shape[0]}\n"
            f"Class names: {cancer['target_names']}\n"
    ) + "\n" + (cancer['DESCR'])
    print(sammanfatning)
    # sparar sammanfattningen i en fil
    with open(path+"database.txt", "w") as f:
        f.write(sammanfatning)
        print("Sammanfattningen är sparad i filen database.txt")
        f.close()

else:
    print("Okej, vi går vidare till nästa steg.")



