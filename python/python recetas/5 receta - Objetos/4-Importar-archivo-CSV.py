# Importar archivo CSV

import pandas as pd 

paises = pd.read_csv('paises.csv')

print(paises.columns) #nombre de las columnas
print()
print(paises.shape) # tamaño del data frame
print()
print(len(paises))  #calcular la cantidad de registros
print()
print(paises['Pais'])  #Ver la solo una columna (Pais) sensible a mayusculas



