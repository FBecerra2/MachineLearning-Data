#Leer el contenido de un archivo

#1. Leer todo el contenido
#2. leer una parte
#3. Utilizar un ciclo

archivo = open('paises.csv')
#1.Lee tdo e contenido del archivo:
#print(archivo.read())

#2.Lee una parte(cantidad en bytes):
#lectura_parcial = archivo.read(10) #10 byte lee del archivo
#print(lectura_parcial)

#3.Uso de un ciclo:

for linea in archivo:
    print(linea, end='') #el end='' omite mostrar el salto de linea