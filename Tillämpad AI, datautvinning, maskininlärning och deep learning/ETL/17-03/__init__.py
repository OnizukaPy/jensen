import os
import pandas as pd
import numpy as np

# FUNCTIONS

# den här funktionen tar en lista med filnamn och returnerar en lista med unika namn
def UniqueName(list_of_files):
    name_list = []
    for name in list_of_files:
        name_list.append(name.split("_"))

    temp = []
    for x in name_list:
        temp.append(x[0])

    df = pd.DataFrame(temp)
    name_list = df[0].unique()

    return name_list

# den här funktionen tar en dataframe och returnerar en dataframe med sorterade kolumner
def RenameColumnsSorted(data):
    columns = list(data)
    columns[0] = "id"
    data.columns = columns
    return data.sort_values(by="id", inplace=True)

# den här funktionen tar en dataframe och sparar den till en csv-fil
def SaveToDb(data, folder, file_name):
    data.to_csv(CURR_DIR_PATH + folder + file_name, index=False)


# MAIN
# hämtar sökvägen till den här filen
# hämtar alla filer i mappen data och sparar dem i en sorterad lista
# hämtar alla unika namn från listan med filnamn
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))
data_files = sorted(os.listdir(CURR_DIR_PATH + "/data"))
name_list = UniqueName(data_files)

# skapar en enkel dataframe som ska innehålla alla dataframes från filer med samma namn

# skapar en tom lista som ska innehålla alla namn av filer som skapas
FILE_DB_LIST = []

# loopar igenom alla unika namn och skapar en ny csv-fil för varje namn
for name in name_list:
    temp = pd.DataFrame()
    for file in data_files:
        if file.startswith(name) and file.endswith(".csv"):
            data = pd.read_csv(CURR_DIR_PATH + "/data/" + file)
            temp = pd.concat([temp, data])

        elif file.startswith(name) and file.endswith(".txt"):
            data = pd.read_csv(
                CURR_DIR_PATH + "/data/" + file,
                sep=",",
                encoding="unicode_escape"
            )
            temp = pd.concat([temp, data])

        temp.to_csv(CURR_DIR_PATH + "/db/" + name + "_data.csv", index=False)
    FILE_DB_LIST.append(name + "_data.csv")

# hanterar alla filer i mappen db för att skapa en ny csv-fil med alla data modifierade
for file in FILE_DB_LIST:
    data = pd.read_csv(CURR_DIR_PATH + "/db/" + file)
    RenameColumnsSorted(data)

    if 'firstname' in data.columns and 'surname' in data.columns:
        data.insert(1,"name",data['firstname'] +' '+ data['surname'],True)
        del data['firstname']
        del data['surname'] 

    if 'attendance' in data.columns:
        data.insert(2, 'late', np.where(data['attendance'] == 60, 0, 60 - data['attendance']), True)
        del data["attendance"]

    SaveToDb(data, "/db/", file) 

# skapar en ny csv-fil med alla data från mappen db
temp = pd.DataFrame()
for file in FILE_DB_LIST:
    data = pd.read_csv(CURR_DIR_PATH + "/db/" + file)
    temp = pd.concat([temp, data])

# sparar den nya csv-filen till mappen results
SaveToDb(temp, "/results/", 'absence_june.csv')

# skriver ut alla personer som är sena mer än 60 minuter
df = pd.read_csv(CURR_DIR_PATH + "/results/" + 'absence_june.csv')
print(df[df['late'] >= 60])
