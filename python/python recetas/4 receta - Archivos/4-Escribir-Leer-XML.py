#Leer contenido de un archivo XML

import xml.etree.ElementTree as ET #importamso el modulo XML y lo renombramos ET

archivo_xml = ET.parse('productos.xml')

raiz = archivo_xml.getroot()

print(raiz)
print()
for hijo in raiz:
    print(hijo.text)

for hijo in raiz:
    print(hijo)