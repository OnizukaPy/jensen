import os

# lista di cartelle e file
path = os.path.dirname(os.path.abspath(__file__))

# importare le credeziali
import json

api = json.load(open(path+'/kaggle.json'))
USERNAME = api['username']
KEY = api['key']

def start_kaggle():
    # impostazione delle variabili d'ambiente per l'autenticazione
    # https://towardsdatascience.com/downloading-datasets-from-kaggle-for-your-ml-project-b9120d405ea4
    os.environ['KAGGLE_USERNAME'] = USERNAME
    os.environ['KAGGLE_KEY'] = KEY

    from kaggle.api.kaggle_api_extended import KaggleApi
    api = KaggleApi()
    api.authenticate()

