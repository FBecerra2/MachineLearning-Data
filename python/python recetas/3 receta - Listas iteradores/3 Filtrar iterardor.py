#Filtrar iterador

numeros  = range(10)

print(list(numeros))

impares_iterador=filter(lambda numero: numero%2, numeros)#lambda tima cada numero de numero y realiza una accion

print(next(impares_iterador))
print(next(impares_iterador))
print(next(impares_iterador))

lista_impares = list(filter(lambda numero: numero%2, numeros))

print(lista_impares)

import itertools #tiene colecciones

lista_pares = list(itertools.filterfalse(lambda numero: numero%2, numeros))

print(lista_pares)
