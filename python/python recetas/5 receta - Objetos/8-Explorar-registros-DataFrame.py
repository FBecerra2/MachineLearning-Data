# Explorar los registros de un Data Frame

# Dos opciones 
# head() Devuelve los 5 primeros regitros 
# podes pasarle un numero para que tome registros ej:head(20) 
# tail() los ultimos 5 registros

import pandas as pd

peliculas = pd.read_csv('movies.csv')

print(peliculas.head())
print()
print(peliculas.columns)
print()



