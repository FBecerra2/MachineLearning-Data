# Crear un dat frame
# data frame en una estuctura de 2 dimensiones. (Columnas y filas)
#Es para analisis de datos

import pandas as pd

diccionario ={'col1':[1, 2, 3, 4, 5], 'col2':[2, 3, 5, 7, 11]}

df = pd.DataFrame(data=diccionario)

print(df.head()) #trae la tabla diccionario
print()
print(df.tail(2)) #trae los dos utimos datos de las columnas
print()
print(df.columns) #trae el nombre de las columnas y tipo
print()
print(df.describe()) # trae estadisticas basicas de las columnas

#count  cantidad de elementos
#mean   media de la columna
#std    desviacion standard
#min    valor minimo
#max    valor maximo
print()
print(df['col2'])
print()
print(type(df['col2']))