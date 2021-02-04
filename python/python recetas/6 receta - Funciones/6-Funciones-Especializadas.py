# todas las funciones son objetos

def generador_multiplicador(multiplo):
    return lambda x: x * multiplo

duplicador = generador_multiplicador(2)

print(duplicador(3))
print(duplicador(5))
print(duplicador(7))


triplicador = generador_multiplicador(3)

print(triplicador(3))
print(triplicador(5))
print(triplicador(7))