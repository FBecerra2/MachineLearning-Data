#Obtener estadisticas basicas en un DataFrame

import pandas as pd 

peliculas = pd.read_csv('movies.csv')

print(peliculas.describe())
print('Media')
print(peliculas.movie_facebook_likes.mean()) #media
print('Minimo')
print(peliculas.movie_facebook_likes.min()) #minimo
print('Maximo')
print(peliculas.movie_facebook_likes.max()) #maximo
