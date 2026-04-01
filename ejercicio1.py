import pandas as pd
import numpy as np  
'''
datos={
    "nombre": ["Juan", "Maria", "Pedro", "Ana", "N/A", "Laura", "Carlos", "Sofia", "Miguel", "Elena"],
    "edad": ["25", "30", "35", "40", "28", "32", "29", "N/A", "33", "34"],
    "altura": ["1.75", "1.65", "1.85", "1.70", "1.80", "1.78", "1.72", "1.68", "1.82", "1.76"],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Malaga", "Zaragoza", "Murcia", "Palma", "Las Palmas"]
}
df= pd.DataFrame(datos)
print(df.info())
df["edad"]= df.edad.astype(int)
df["altura"]= df.altura.astype(float)
print(df.describe())

print(df.describe())
print(df.head())
print(df.tail())
datos["edad"]= pd.to_numeric(datos["edad"])
datos["altura"]= pd.to_numeric(datos["altura"])

'''
nuevo= pd.DataFrame({
    "nombre": ["Juan", "Maria", "Pedro", "Ana", "N/A", "Laura", "Carlos", "Sofia", "Miguel", "Elena"],
    "edad": [25, 30, 35, 40, 28, 32, 29, np.nan, 33, 34],
    "altura": [1.75, 1.65, 1.85, 1.70, 1.80, 1.78, 1.72, 1.68, 1.82, 1.76],
    "ciudad": ["Madrid", "Barcelona", "Valencia", "Sevilla", "Bilbao", "Malaga", "Zaragoza", "Murcia", "Palma", "Las Palmas"]
})
print(nuevo.describe())
nuevo= nuevo.replace("N/A", np.nan)
print(nuevo)

