#Importar archivo de excel
#Instalar pip install xlrd
import pandas as pd 

df = pd.read_excel('paises.xlsx', sheet_name='suramerica')

print(df.head())