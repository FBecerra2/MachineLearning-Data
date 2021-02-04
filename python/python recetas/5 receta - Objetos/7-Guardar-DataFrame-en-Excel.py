# Guardar contenido DataFrame en un Archivo de Excel

import pandas as pd

ids = [1, 2, 3, 4, 5]

paises_europeos = ['Albania', 'Belgica', 'Chipre', 'Eslovenia', 'Dinamarca']

df = pd.DataFrame(data={'id': ids, 'pais': paises_europeos})

print(df.head())
#install pip install openpyxl
df.to_excel('paises_europeos.xlsx', sheet_name='europa', index=False)
