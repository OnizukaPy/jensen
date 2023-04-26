import api_smhi as smhi
import pandas as pd

w = smhi.SMHI()

data = w.get_data_from_smhi(2, 58)

lista = ["temperature", "air pressure", "precipitation"]

for i in lista:
    w.to_plot(i)

