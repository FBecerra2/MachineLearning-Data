# Remover el espacio o cualquier otro caracter de una cadena de caracteres

lenguaje = '   Python es genial  '

frase = 'xxxyyyxxx'
print(lenguaje)

print(lenguaje.strip())

print(frase.strip('x')) # remueve la x de la variable frase

#rstip(),remueve caracter a la derecha
# lstrip() remueve caracteres a la izquierda

print(frase.lstrip('x').rstrip('x'))