# Guardar contenido DataFrame en archivo CSV

import pandas as pd 

paises = ['Albania','Belgica','Chipre','Eslovenia','Dinamarca','España']

paises_df = pd.DataFrame(data={'pais': paises}) #armamos el dataframe

print(paises_df) #Genera una lista con los paises y le asigna un ID

print()

paises_df.to_csv('paises_europeos.csv', index=False) #index elimina el indice