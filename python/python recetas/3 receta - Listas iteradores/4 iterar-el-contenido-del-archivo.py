# Iterar el contenido de un archivo

archivo = open('paises.csv')

for pais in archivo:
    print(pais)

archivo = open('paises.csv')
print(next(archivo))