#Obtener metadatos de un directotorio

import os

directorio_actual =os.getcwd()

print(directorio_actual)

metadatos = os.stat(directorio_actual)

print(metadatos)

print(metadatos.st_ctime)