# Decimales con presiicon arbitraria

from decimal import *

print(getcontext())
print(Decimal(1)/Decimal(3)) # Division que trae hasta 28 decimales

getcontext().prec = 7

print(Decimal(1)/Decimal(3)) # Limita la salida a 7 decimales

