#Crear Objeto Series

#objetos de la libreria panda
#Sirve apra Data Science
#instalamos panda en terminal pip install panda

import pandas as pd

print(pd.__version__)

#sirius representa una variable o entidad de data frame

datos = [1, 2, 3, 4, 5]

serie = pd.Series(datos) # lo introducimos en una serie

print(serie)   #muestra la posicion y el numero

print(serie * 5) # muestra la posicion y el numero multiplicado por 5

print(serie.dtype) # muestra el tipo de dato de la serie

