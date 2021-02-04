#Crear archivo Zip

from zipfile import ZipFile

nuevo_archivo = ZipFile('archivo.zip', 'a') #a = append agregar
#aca va la lista de archos que quiero en el zip
nuevo_archivo.write('paises.csv')
nuevo_archivo.write('productos.xml')

nuevo_archivo.close() #Aca paso que termina de agrear archivos al zip