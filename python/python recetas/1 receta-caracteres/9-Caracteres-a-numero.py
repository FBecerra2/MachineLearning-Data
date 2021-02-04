# Conversion de cadena de caracteres en valores numericos
#int() , float(), long() y complex()

literal_enterero = '123'
literal_decimal = '3.1415'
literal_entero_largo = '12345678905678905678954678'
literal_complejo = '5+8j'

entero = int(literal_enterero)
print(type(literal_enterero))

print(entero)

decimal = float(literal_decimal)
print(type(literal_decimal))

print(decimal)
#Sirve para Python viejo
#entero_largo = long(literal_entero_largo)
#print(type(entero_largo))
#print(entero_largo)

entero_largo = int(literal_entero_largo)
print(type(entero_largo))
print(entero_largo)

complejo = complex(literal_complejo)
print(type(complejo))

print(complejo)