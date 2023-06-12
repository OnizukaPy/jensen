from autenticazione.autenticazione import USERNAME, KEY
import os

path = os.path.dirname(os.path.abspath(__file__))
print(path)
# impostazione delle variabili d'ambiente per l'autenticazione in alternativa al 'kaggle.json'
# https://towardsdatascience.com/downloading-datasets-from-kaggle-for-your-ml-project-b9120d405ea4
os.environ['KAGGLE_USERNAME'] = USERNAME
os.environ['KAGGLE_KEY'] = KEY

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()

# Visualizzare la lista dei dataset
import pandas as pd
import kaggle
datasets = kaggle.api.datasets_list(search="covid")

for dataset in datasets:
    print(dataset['ref'])
    
kaggle.api.dataset_download_files('sudalairajkumar/covid19-in-italy', path=path+'/dataset', unzip=True)


