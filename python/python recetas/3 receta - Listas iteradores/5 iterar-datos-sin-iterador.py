# Iterar daros que no tienen un iterador

def generar_cuadrado(valor = 0):
    while True:
        valor += 1

        yield (valor -1) ** 2  #permite devolver una funcion diferente pasandole un valor diferente a yield

generador = generar_cuadrado()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#tenemos una conexion a BBDD podemos usar esto

generador = generar_cuadrado(5)
print()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))