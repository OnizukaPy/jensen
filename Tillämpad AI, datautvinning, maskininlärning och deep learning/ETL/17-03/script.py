import __init__ as init
import pandas as pd


for name in init.FILE_DB_LIST:

    data = pd.read_csv(init.CURR_DIR_PATH + "/db/" + name)
    if 'firstname' in data.columns and 'surname' in data.columns:
        data.insert(1,"name",data['firstname'] +' '+ data['surname'],True)
        del data['firstname']
        del data['surname'] 
    data.to_csv(init.CURR_DIR_PATH + "/db/" + name, index=False)

