#Iterar el contenido de un directorio

import pathlib

p = pathlib.Path('.')

for elemento in p.iterdir():
    print(elemento)