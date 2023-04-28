import json
import requests as r
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

# url för att hämta data från SMHI
category = "pmp3g"
version = "2"
url = "https://opendata-download-metfcst.smhi.se"
PARAMS = f"/api/category/{category}/version/{version}/parameter.json"

# Objekt för att hämta data från SMHI
class SMHI:

    def __init__(self):
        self.data = None        # attribut för att lagra data från SMHI

    # Hämtar rådata från SMHI och skapar en dictionary
    def get_data_from_smhi(self, lon, lat, path, name):
        # hämtar data från SMHI med hjälp av url API och skapar en json variabel
        data = r.get(f"{url}/api/category/{category}/version/{version}/geotype/point/lon/{lon}/lat/{lat}/data.json").json()
        # skapar en dataframe från timeSeries nyckeln i json variabel
        df = pd.DataFrame(data['timeSeries'])

        # kör en loop för att skapa en dictionary med data från dataframe df
        dict = []
        for i in range(len(df)):
            temp = {}
            pf = pd.DataFrame(df['parameters'][i], columns=['name', 'values'])
            temp['validTime'] = df['validTime'][i]
            for j in pf['name']:
                temp[j] = pf[pf['name'] == j]['values'].values[0][0]            # för att ta ur värdet från listan. Value är en lista i början
            dict.append(temp)

        # skapar en dataframe från dictionary
        dataframe = pd.DataFrame(dict)
        # skapar en dictionary med data från dataframe
        self.data = {}
        self.data["date"] = dataframe['validTime'].tolist()
        self.data["temperature"] = dataframe['t'].tolist()
        self.data["air pressure"] = dataframe['msl'].tolist()
        self.data["precipitation"] = dataframe['pmax'].tolist()

        # skapar en json fil med data
        with open(f'{path}{name}.json', 'w') as f:
            json.dump(self.data, f)
        print(f"Modified data saved to {name}.json")

        return self.data

    # plotta hanterad data från SMHI och spara som png fil
    def to_plot(self, name, url):
        self.data["date"] = pd.to_datetime(self.data["date"])
        gf = pd.DataFrame(self.data, columns=["date", name])
        gf.plot(x="date", y=name, kind="line")
        plt.savefig(f'{url}{name}.png')
        print(f"Graphic saved to {name}.png")
    
    # spara hanterad data från SMHI till en databas
    def to_sql(self, table, database_url):
        df = pd.DataFrame(self.data)
        df["date"] = pd.to_datetime(df["date"])
        engine = create_engine(database_url)
        engine.execute(f"DROP TABLE IF EXISTS {table}")
        df.to_sql(table, engine, if_exists="append", index=False)
        print(f"Data saved to {database_url}")

        