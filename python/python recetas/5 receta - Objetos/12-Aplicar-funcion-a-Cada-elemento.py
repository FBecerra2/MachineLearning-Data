#Aplicar una funcion a cada elemento de un DataFrame o Series

import pandas as pd 
import numpy as np
datos = {'col1':[1,2,3], 'col2':[4,5,6], 'col3':[7,8,9]}

#1. applymap: se usa sobre un DataFrame
#2. map: se usa sobre un series
df = pd.DataFrame(data=datos)

print(df.apply(lambda x: x ** 3)) #eleva todo al cubo

print(df.col2.map(lambda x: x ** 2)) #Eleva solo la segunda columna

