# Copiar un archivo

#funciones para archivos copy()

import shutil

ruta_nuevo_archivo = shutil.copy('paises.csv', 'paises2.csv')

print(ruta_nuevo_archivo)

#copy2() coppia la metadata del archivo original.

