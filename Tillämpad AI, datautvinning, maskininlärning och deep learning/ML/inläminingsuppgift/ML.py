# linear regression: GridSearchCV, RandomizedSearchCV (Ridge, Lasso)
# logistic regression: med PCA, utan PCA
# ForestRandomClassifier
# accuracy_score, confusion matrix, classification report, cross_val_score

import database as DB
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.decomposition import PCA
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def select_features(X_train, y_train, X_test):
    # Find a good subset of features

    fs = SelectFromModel(RandomForestClassifier(n_estimators=100, random_state=42), threshold=0.08)
    fs.fit(X_train, y_train)
    X_train_fs = fs.transform(X_train)
    print("X_train_fs: ", X_train_fs.shape, "X_train: ", X_train.shape)
    X_test_fs = fs.transform(X_test)
    print("X_test_fs: ", X_test_fs.shape, "X_test: ", X_test.shape)

    return X_train_fs, X_test_fs, fs

class ML:
    def __init__(self, df, best_features, rs):
        self.df = df
        self.best_features = best_features
        self.X = self.df[self.best_features]
        self.y = np.where(self.df['target'] == 'malignant', 1, 2)
        self.random_state = rs

    def pca_analysis(self, show=False):
        self.pca = PCA(n_components=2)
        self.X_pca = self.pca.fit_transform(self.X)
        self.df_pca = pd.DataFrame(data = self.X_pca, columns = ['pca1', 'pca2'])
        self.df_pca['target'] = self.y
        self.y_pca = self.y

        if show == True:
            plt.figure(figsize=(10,8))
            sns.scatterplot(x="pca1", y="pca2", data=self.df_pca, hue="target", palette="Set1")
            plt.xlabel("PC1")
            plt.ylabel("PC2")
            plt.title("PCA om Bröst Cancer dataset")
            plt.legend()
            plt.show()   
            print("PCA analysis is done")        

    def split_data(self, pca, show):
        if pca == True:
            self.pca_analysis(show)
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_pca, self.y_pca, test_size=0.3, random_state=self.random_state)
            print("Data is splitted into train and test with PCA")

        elif pca == False:
            self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.3, random_state=self.random_state)
            print("Data is splitted into train and test without PCA")
        else:
            print("pca must be True or False")
        
    
    def linear_regression(self, pca):

        self.split_data(pca, show=False)
        self.lin_reg = LinearRegression()
        self.lin_reg.fit(self.X_train, self.y_train)
        self.y_pred = self.lin_reg.predict(self.X_test)

        self.mse = mean_squared_error(self.y_test, self.y_pred)
        self.mae = mean_absolute_error(self.y_test, self.y_pred)
        self.r2 = r2_score(self.y_test, self.y_pred)
        self.score = self.lin_reg.score(self.X_test, self.y_test)

        print('\n')
        print(f"PCA: {pca}")
        print(f"Mean squared error: {self.mse}\nMean absolute error: {self.mae}\nR2 score pred: {self.r2}\nScore test: {self.score}")

        return self.score
    
    def logistic_regression(self, pca):

        self.split_data(pca, show=False)        
        self.log_reg = LogisticRegression()
        self.log_reg.fit(self.X_train, self.y_train)
        self.y_pred = self.log_reg.predict(self.X_test)

        self.accuracy_score = accuracy_score(self.y_test, self.y_pred)
        self.cross_val_score = cross_val_score(self.log_reg, self.X, self.y, cv=5)
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
        self.classification_report = classification_report(self.y_test, self.y_pred)

        print('\n')
        print(f"PCA: {pca}")
        print(f"Accuracy score: {self.accuracy_score}\nCross val score: {self.cross_val_score}\n")
        print(self.classification_report)
        print('\n')
        print(f"TP: {self.confusion_matrix[0][0]}\nFP: {self.confusion_matrix[0][1]}\nFN: {self.confusion_matrix[1][0]}\nTN: {self.confusion_matrix[1][1]}")
    
        return self.accuracy_score

    def forest_random_class(self, pca):

        self.split_data(pca, show=False)
        self.forest_random = RandomForestClassifier(n_estimators=100, random_state=self.random_state)
        self.forest_random.fit(self.X_train, self.y_train)
        self.y_pred = self.forest_random.predict(self.X_test)

        self.importances = self.forest_random.feature_importances_
        plt.bar([x for x in range(len(self.importances))], self.importances)
        plt.show()

        self.X_train_fs, self.X_test_fs, self.fs = select_features(self.X_train, self.y_train, self.X_test)

        self.forest_random_fs = RandomForestClassifier(n_estimators=100, random_state=self.random_state)
        self.forest_random_fs.fit(self.X_train_fs, self.y_train)
        self.y_pred_fs = self.forest_random_fs.predict(self.X_test_fs)

        self.accuracy_score = accuracy_score(self.y_test, self.y_pred_fs)
        self.cross_val_score = cross_val_score(self.forest_random_fs, self.X, self.y, cv=5)
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred_fs)
        self.classification_report = classification_report(self.y_test, self.y_pred_fs)

        print('\n')
        print(f"PCA: {pca}")
        print(f"Accuracy score: {self.accuracy_score}\n")
        print(self.classification_report)
        print('\n')
        print(f"TP: {self.confusion_matrix[0][0]}\nFP: {self.confusion_matrix[0][1]}\nFN: {self.confusion_matrix[1][0]}\nTN: {self.confusion_matrix[1][1]}")

        return self.accuracy_score

    def KNC(self, pca):
        self.split_data(pca, show=False)
        self.knc = KNeighborsClassifier(n_neighbors=5, metric='euclidean')
        self.knc.fit(self.X_train, self.y_train)
        self.y_pred = self.knc.predict(self.X_test)

        self.accuracy_score = accuracy_score(self.y_test, self.y_pred)
        self.cross_val_score = cross_val_score(self.knc, self.X, self.y, cv=5)
        self.confusion_matrix = confusion_matrix(self.y_test, self.y_pred)
        self.classification_report = classification_report(self.y_test, self.y_pred)

        print('\n')
        print(f"Accuracy score: {self.accuracy_score}\nCross val score: {self.cross_val_score}\n")
        print(self.classification_report)
        print('\n')
        print(f"TP: {self.confusion_matrix[0][0]}\nFP: {self.confusion_matrix[0][1]}\nFN: {self.confusion_matrix[1][0]}\nTN: {self.confusion_matrix[1][1]}")

        return self.accuracy_score

    def complete_analysis(self):
        print('PCA analysis\n')
        self.pca_analysis(True)
        print('\nLinear regression\n')
        lr_pca = self.linear_regression(True)
        lr = self.linear_regression(False)
        print('\nLogistic regression\n')
        log_reg_pca = self.logistic_regression(True)
        log_reg = self.logistic_regression(False)
        print('\nForest random\n')
        forest_random = self.forest_random_class(False)
        print('\nKNeighborsClassifier\n')
        knc_pca = self.KNC(True)
        knc = self.KNC(False)
        
        df_temp = pd.DataFrame({'Linear regression': [lr_pca, lr], 'Logistic regression': [log_reg_pca, log_reg], 'Forest random': [np.NaN, forest_random], 'KNC': [knc_pca, knc]})
        df_temp.index = ['PCA', 'No PCA']

        return df_temp