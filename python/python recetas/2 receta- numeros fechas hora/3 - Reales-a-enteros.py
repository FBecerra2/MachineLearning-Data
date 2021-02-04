#Redondear reales a entereos

pi = 3.1415

#1. int()
#2 .trunc()   del paquete math
#3. round()


## primera forma
print(type(pi))
print(int(pi))
print(type(int(pi)))

##segunda forma

from math import trunc

print()
print(trunc(pi))

##Tercera forma

print(round(pi))