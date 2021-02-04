# Guardar datos como objetos enmemoria secundaria

import pickle

#paises = {'Colombia': 'Bogota', 'Argentina': 'Buenas Aires'}

#archivo_paises = open('paises.pickle', 'wb') ## w = write b = binario

#pickle.dump(paises, archivo_paises)

archivo = open('paises.pickle', 'rb') ## r = read b= binario

paises_recuperados = pickle.load(archivo)

print(paises_recuperados)