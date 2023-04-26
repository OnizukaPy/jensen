
import json
import requests as r
import pandas as pd
import matplotlib.pyplot as plt

# den här funktionen konverterar grader till numeriska värden
def degrees_to_numeric(d):
    b = []
    for item in d:
        b.append(item[0])
    return b


# url för att hämta data från SMHI
category = "pmp3g"
version = "2"
url = "https://opendata-download-metfcst.smhi.se"
PARAMS = f"/api/category/{category}/version/{version}/parameter.json"

# Objekt för att hämta data från SMHI
class SMHI:

    def __init__(self):
        self.data = None
    # Hämtar data från SMHI och skapar en dictionary
    def get_data_from_smhi1(self, lon, lat):
        self.data = r.get(f"{url}/api/category/{category}/version/{version}/geotype/point/lon/{lon}/lat/{lat}/data.json").json()
        return self.data
    
    # Hämtar data från SMHI och skapar en dictionary
    def get_data_from_smhi(self, lon, lat):
        data = r.get(f"{url}/api/category/{category}/version/{version}/geotype/point/lon/{lon}/lat/{lat}/data.json").json()
        # skapar en dataframe från data med timeSeries som index
        df = pd.DataFrame(data['timeSeries'])

        # kör en loop för att skapa en dictionary med data från dataframe
        dict = []
        for i in range(len(df)):
            temp = {}
            pf = pd.DataFrame(df['parameters'][i], columns=['name', 'values'])
            temp['validTime'] = df['validTime'][i]
            for j in pf['name']:
                temp[j] = pf[pf['name'] == j]['values'].values[0]
            dict.append(temp)

        # skapar en dataframe från dictionary
        dataframe = pd.DataFrame(dict)
        # skapar en dictionary med data från dataframe och konverterar grader till numeriska värden
        self.data = {}
        self.data["date"] = dataframe['validTime'].tolist()
        self.data["temperature"] = dataframe['t'].tolist()
        self.data["air pressure"] = dataframe['msl'].tolist()
        self.data["precipitation"] = dataframe['pmax'].tolist()

        with open(f'data.json', 'w') as f:
            json.dump(self.data, f)

        return self.data

    def to_plot(self, name):
        self.data["date"] = pd.to_datetime(self.data["date"])
        self.data[name] = degrees_to_numeric(self.data[name])
        gf = pd.DataFrame(self.data, columns=["date", name])
        gf.plot(x="date", y=name, kind="line")
        plt.show()

        