#Mapear caracteres de un objeto string

lenguaje ='Pithon'

mapa = lenguaje.maketrans('i','y')
print(lenguaje)
print(lenguaje.translate(mapa))

lenguaje = 'pyt       hon'
print(lenguaje)
lenguaje = lenguaje.translate(str.maketrans({' ': None})) #para borrar espacion vacios

print(lenguaje)
