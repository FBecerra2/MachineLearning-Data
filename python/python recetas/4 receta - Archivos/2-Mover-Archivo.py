# Mover Archivo de un dir a otro

import shutil
shutil.copy('paises.csv', 'paises2.csv')
shutil.move('paises2.csv','sub_directorio',copy_function=shutil.copy)
