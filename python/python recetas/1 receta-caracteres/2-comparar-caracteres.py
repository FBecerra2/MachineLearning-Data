# ==: a nivel de contenido
# is: a nivel de referencia

lenguaje = 'Python'

if lenguaje == 'python':
    print('Las cadenas son iguales')
else:
    print('No son iguales')

lenguaje_python = lenguaje

if lenguaje is lenguaje_python:
    print('Son iguales.')
else:
    print('No son iguales.')