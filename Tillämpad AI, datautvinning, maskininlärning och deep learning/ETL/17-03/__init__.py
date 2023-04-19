import os
import pandas as pd
import numpy as np

# FUNCTIONS

def UnqueName(list_of_files):
    name_list = []
    for name in list_of_files:
        name_list.append(name.split("_"))

    temp = []
    for x in name_list:
        temp.append(x[0])

    df = pd.DataFrame(temp)
    name_list = df[0].unique()

    return name_list

def RenameColumnsSorted(data):
    columns = list(data)
    columns[0] = "id"
    data.columns = columns
    return data.sort_values(by="id", inplace=True)

def SaveToDb(data, folder, file_name):
    data.to_csv(CURR_DIR_PATH + folder + file_name, index=False)


# MAIN
CURR_DIR_PATH = os.path.dirname(os.path.realpath(__file__))

data_files = sorted(os.listdir(CURR_DIR_PATH + "/data"))
name_list = UnqueName(data_files)

FILE_DB_LIST = []

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

for file in FILE_DB_LIST:
    data = pd.read_csv(CURR_DIR_PATH + "/db/" + file)
    RenameColumnsSorted(data)

    if 'firstname' in data.columns and 'surname' in data.columns:
        data.insert(1,"name",data['firstname'] +' '+ data['surname'],True)
        del data['firstname']
        del data['surname'] 

    if 'attendance' in data.columns:
        #data['late'] = np.where(data['attendance'] == 60, 0, 60 - data['attendance'])
        data.insert(2, 'late', np.where(data['attendance'] == 60, 0, 60 - data['attendance']), True)
        del data["attendance"]
        #data.rename(columns={'attendance': 'late'}, inplace=True)

    SaveToDb(data, "/db/", file)

temp = pd.DataFrame()
for file in FILE_DB_LIST:
    data = pd.read_csv(CURR_DIR_PATH + "/db/" + file)
    temp = pd.concat([temp, data])

SaveToDb(temp, "/results/", 'absence_june.csv')

df = pd.read_csv(CURR_DIR_PATH + "/results/" + 'absence_june.csv')

print(df[df['late'] >= 60])
