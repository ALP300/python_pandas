import pandas as pd
import numpy as np

datos= pd.read_csv("ATP_DATA.csv", encoding="latin1")
print(datos.head())
print(datos.info())
nuevo= pd.DataFrame(datos)
nuevo2= pd.DataFrame(datos)
print(datos.describe())
nuevo2= nuevo2.replace("N/A", "0")
nuevo2= nuevo2.replace("NR", "0")
nuevo2['Wsets']= pd.to_numeric(nuevo2['Wsets'])
nuevo2['Lsets']= pd.to_numeric(nuevo2['Lsets'])
nuevo2['WRank']= pd.to_numeric(nuevo2['WRank'])
nuevo2['LRank']= pd.to_numeric(nuevo2['LRank'])
print(nuevo2.info())
print(nuevo2)