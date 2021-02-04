# Modulo itertools

#accumulate()
#combinations()

rango = range(10)

# 0 1 2 3 4 5 6 7 8 9
#0 1 3 5...

import itertools          #fibonacci
acumulador = itertools.accumulate(rango)

print(next(acumulador))
print(next(acumulador))
print(next(acumulador))
print(next(acumulador))
print(next(acumulador))

combinaciones = itertools.combinations(rango, 2)
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))
print(next(combinaciones))

