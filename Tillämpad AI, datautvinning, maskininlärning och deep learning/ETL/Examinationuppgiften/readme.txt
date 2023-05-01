ETL Examinationsprojekt

Gruppmedlemmar:
Ivan Catalano och Bruno Silva


Beskrivning


Koden är delat i två script:


I api_smhi.py fil:

Den här script heter api_smhi.py. Och har alla funktioner till koden.

Här använder vi följande moduler;

- JSON, för att hantera data som var skrivit på Java Script;

- Requests för att använda HTTP för att ropa URL´s.;

- Pandas för att hanterar alla data,

- Matplotlib.pyplot för att visa data med grafiker;

- Sqlalchemy för att skaffa databasen och spara alla data I en database.


1. - 

category = "pmp3g"
version = "2"
url = "https://opendata-download-metfcst.smhi.se"
PARAMS = f"/api/category/{category}/version/{version}/parameter.json"

Den här koden, skaffar 3 variabler. Då gör en API request och hämtar data.


2. -

def get_data_from_smhi(self, lon, lat, path, name):

data = r.get(f"{url}/api/category/{category}/version/{version}/geotype/point/lon/{lon}/lat/{lat}/data.json").json()


df = pd.DataFrame(data['timeSeries'])

Första del av funktionen get_data_from_smhi skaffa en variable “data” som hämtar data från API och sparar som Json. Efteråt variablen “df” skaffar en dataframe med dessa data.


3. - 

for i in range(len(df)):
            temp = {}
            pf = pd.DataFrame(df['parameters'][i], columns=['name', 'values'])
            temp['validTime'] = df['validTime'][i]
            for j in pf['name']:
                temp[j] = pf[pf['name'] == j]['values'].values[0][0] 
            dict.append(temp)


Andra del av funktionen kör en loop för att omvända “DataFrame” till en dictionary med kolumner “Name” och “Values”.


4 - 

        dataframe = pd.DataFrame(dict)

        self.data = {}
        self.data["date"] = dataframe['validTime'].tolist()
        self.data["temperature"] = dataframe['t'].tolist()
        self.data["air pressure"] = dataframe['msl'].tolist()
        self.data["precipitation"] = dataframe['pmax'].tolist()


Tredje del av funktionen, skaffar en dataFrame som efteråt, fyller den ny dictionary med data från “self.data”. Kolumner är också skaffat.


5. -

with open(f'{path}{name}.json', 'w') as f:
            json.dump(self.data, f)
        print(f"Modified data saved to {name}.json")

        return self.data

Sista delen av funktionen skaffar en Json file. “w” argumentet betyder att vi får skriva och ändrar data. Med json.dump är hanterade data sparat I in json filen.


6. -

def to_plot(self, name, url):
        self.data["date"] = pd.to_datetime(self.data["date"])
        gf = pd.DataFrame(self.data, columns=["date", name])
        gf.plot(x="date", y=name, kind="line")
        plt.savefig(f'{url}{name}.png')
        print(f"Graphic saved to {name}.png")

Funktionen to_plot, skaffar en linja men istället av vissa en grafik, sparar som en bild.


7. -

def to_sql(self, table, database_url):
        df = pd.DataFrame(self.data)
        df["date"] = pd.to_datetime(df["date"])
        engine = create_engine(database_url)
        engine.execute(f"DROP TABLE IF EXISTS {table}")
        df.to_sql(table, engine, if_exists="append", index=False)
        print(f"Data saved to {database_url}")

Funktionen to_sql, sparar data till database tabeller med “engine”. Med “append”, är data sparat I database, istället att försvinna när databasen stängar. 



I Examination.py fil:

Den här script är “huvud” filen, alltså, gör koden att fungera.

Allt från api_smhi.py är importerad (funktioner)

Module os är använt för att hitta filen.


1. -

PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
DBNAME = 'data.db'
SQLLITE = 'sqlite:///'+PATH+DBNAME

Första del av koden skaffar en variable “PATH” ger “vägen” till mappen var data bör spara I, skaffa database och “SQLLITE” kopplar database till path (mapp som gäller).


2. -

w = smhi.SMHI()

Här är en instans av klassen SMHI skaffat.


3. -

data = w.get_data_from_smhi(2, 58, PATH, "data")
w.to_sql("weather", SQLLITE)

Med get_data_from_smhi funktionen, är data plockat upp från API och sparat I “data” variable I in “path”. Siffror “2” och “58” betyder longitud och latitud från orten.
Med to_sql funktionen är data sparat I en dabase som ligger var “SQLLITE” pekar ut.


4. -

lista = ["temperature", "air pressure", "precipitation"]

for i in lista:
    w.to_plot(i, PATH)

Till slut, en lista är skaffat med samma kolumner namm som I dataFrame I api_smhi.py fil.
Efteråt kör en loop som ger värden från SMHI till lista (I) och sparar I “path” som en bild (png).
