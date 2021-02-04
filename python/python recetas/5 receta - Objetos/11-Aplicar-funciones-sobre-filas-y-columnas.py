#Aplicar una funcion sobre una fila o una columna

import pandas as pd 
import numpy as np
datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

df  = pd.DataFrame(data=datos, index=['b','c','a'])

print(df.apply(np.mean)) #Da el promedio de cada fila

print(df.apply(np.mean, axis=1)) # [promedio de columnas]

print(df.apply(lambda x: 2 * x)) #multiplicar cada elemento 
#por 2 se puede hacer por columna o fila


