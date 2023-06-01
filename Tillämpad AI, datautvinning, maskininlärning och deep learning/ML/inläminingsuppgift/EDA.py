import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

import database as DB

import time
sleep_time = 0.5

class EDA:

    def __init__(self, df):
        self.df = df                
    
    def plot_correlation_matrix(self):

        plt.figure(figsize=(20, 20))
        sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm', linewidths=0.2)
        plt.title('Correlation matrix')
        plt.savefig(DB.PATH + "images/database/" + 'correlation_matrix.png')
        #plt.show()

        return "Correlation matrix is saved in the file correlation_matrix.png"
    
    def plot_count_target(self):
        sns.countplot(x = "target", data = self.df)
        plt.savefig(DB.PATH + "images/database/" + 'count_target.png')
        #plt.show()

        return "Count target is saved in the file count_target.png"

    def plot_pairplot(self):
        sns.pairplot(self.df, hue="target", height=2)
        plt.savefig(DB.PATH + "images/database/" + 'pairplot.png')
        #plt.show()

        return "Total correlations is saved in the filename pairplot.png"
    
    def plot_feature_distribution(self):

        self.df.hist(figsize=(20, 20))
        plt.savefig(DB.PATH + "images/database/"+'feature_distribution.png')
        #plt.show()

        return "Feature distribution is saved in the file feature_distribution.png"
    
    def define_best_features(self, n):

        if n >= 1 or n <= 0:
            return "The value of n must be between >0 and <1"
        else:
            corr = self.df.corr()
            result = []
            for i in range(len(corr.columns)):
                for j in range(i):
                    if abs(corr.iloc[i, j]) > n and abs(corr.iloc[i, j]) < 1:
                        name_i = corr.columns[i]
                        name_j = corr.columns[j]
                        result.append([name_i, name_j, corr.iloc[i, j]])
            
            sorted_corr = sorted(result, key=lambda x: x[2], reverse=True)
            
            # skapa en lista av kolumner son vill använda för att träna modellen
            temp = np.array([])
            for i in range(len(sorted_corr)):
                temp = np.append(temp, sorted_corr[i][1])
                temp = np.append(temp, sorted_corr[i][0])

            # ta bort dubletter
            self.best_features = np.unique(temp)

            return self.best_features
        
    def plot_boxplot(self):

        for i in range(len(self.best_features)):
            plt.figure(figsize=(10, 10))
            sns.boxplot(x='target', y=self.best_features[i], data=self.df)
            plt.savefig(DB.PATH + "images/EDA/" + f'boxplot_{self.best_features[i]}.png')
            #plt.show()

        return "Boxplots are saved in the files EDA"

db = DB.set_db()
df = DB.set_df(db)
eda = EDA(df)
eda.plot_pairplot()







