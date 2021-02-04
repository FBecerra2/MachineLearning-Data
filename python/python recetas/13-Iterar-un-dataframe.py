#Iterar un DataFrame
import pandas as pd 
import numpy as np
datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

df = pd.DataFrame(data=datos)

# iteracion por columnas

for columna in df: #obtener columnas de un DataFrame
    print(columna)

for columna in df: #ver columnas y sus datos
    print(df[columna])

#Ierar indice fla

for indice, fila in df.iterrows():
    print('Indice:{}'.format(indice)) #muestra la palabra indie con el indice
    print(fila) # muestra los valos para cada una de la fila de la columna

    