import api_smhi as smhi
import pandas as pd
import os

PATH = os.path.abspath(os.path.dirname(__file__)) + '/'
DBNAME = 'data.db'
SQLLITE = 'sqlite:///'+PATH+DBNAME

w = smhi.SMHI()

data = w.get_data_from_smhi(2, 58)
w.to_sql("weather", SQLLITE)

lista = ["temperature", "air pressure", "precipitation"]

for i in lista:
    w.to_plot(i, PATH)

