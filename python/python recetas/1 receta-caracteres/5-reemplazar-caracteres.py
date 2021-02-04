# Reemplazar texto en na cadena de caracteres

frase = 'python.com es el sitio oficial de Python'

# Forma manual: uso de la notacion slicing

frase_corregida = frase[0:7] + 'org' + frase[10:]

print(frase_corregida)

#Forma automatica : uso del metodo replace

frase_corregida = frase.replace('com', 'org')

print(frase_corregida)