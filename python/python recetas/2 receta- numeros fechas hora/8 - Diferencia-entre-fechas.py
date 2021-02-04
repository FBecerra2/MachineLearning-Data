# Diferencia entre horas y fechas

import datetime  # importa el modulo de fecha
import time     # importa simulador de tiempo

fecha1 = datetime.datetime.now()
time.sleep(3)
fecha2 = datetime.datetime.now()

diferencia = (fecha2 - fecha1)

print(diferencia.seconds)

delta = datetime.timedelta (days=7)

fecha_resultado = fecha2 + delta

print(fecha2.day)
print(fecha_resultado.day)