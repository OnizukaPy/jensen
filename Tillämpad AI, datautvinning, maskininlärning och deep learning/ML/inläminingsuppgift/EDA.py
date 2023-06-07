# importera bibliotek som behövs för att hantera data och visualisera den
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# importera moduler och bibliotek som behövs för att använda mappen 
import database as DB

# skapa en klass för att utföra EDA
class EDA:

    def __init__(self, df):
        self.df = df                
    
    # skapa en metod för att skriva ut en matris med korrelationer
    def plot_correlation_matrix(self):

        plt.figure(figsize=(20, 20))
        sns.heatmap(self.df.corr(), annot=True, cmap='coolwarm', linewidths=0.2)
        plt.title('Correlation matrix')
        plt.savefig(DB.PATH + "images/database/" + 'correlation_matrix.png')
        #plt.show()

        return "Correlation matrix is saved in the file correlation_matrix.png"

    # skapa en metod för att skriva ut grafen pairplot med den besta variablerna 
    def plot_pairplot(self, array):
        sns.pairplot(self.df[array], hue="target", height=2)
        plt.savefig(DB.PATH + "images/database/" + 'pairplot.png')
        #plt.show()

        return "Total correlations is saved in the filename pairplot.png"
    
    # skapa en metod för att skriva ut en bil med alla histogram för alla variabler
    def plot_feature_distribution(self):

        self.df.hist(figsize=(20, 20))
        plt.savefig(DB.PATH + "images/database/"+'feature_distribution.png')
        #plt.show()

        return "Feature distribution is saved in the file feature_distribution.png"
    
    # skapa en metod för att spara en lista med de bästa variablerna, dvs de som har högst korrelationer.
    # n är en parameter som används för att välja de bästa variablerna.
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
            
            temp = np.array([])
            for i in range(len(sorted_corr)):
                temp = np.append(temp, sorted_corr[i][1])
                temp = np.append(temp, sorted_corr[i][0])

            self.best_features = np.unique(temp)

            return self.best_features
    
    # skapa en metod för att skriva ut boxplots bilder för alla besta variabler
    def plot_boxplot(self):

        for i in range(len(self.best_features)):
            plt.figure(figsize=(10, 10))
            sns.boxplot(x='target', y=self.best_features[i], data=self.df)
            plt.savefig(DB.PATH + "images/EDA/" + f'boxplot_{self.best_features[i]}.png')
            #plt.show()

        return "Boxplots are saved in the files EDA"



