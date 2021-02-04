#Operaiones con numeros complejos
class(3+2i)

(3+2i)*5

(3+2i)*(-1+3i)

(3+2i)/(-1+3i)

#Raiz Cuadrada de numero complejo

sqrt(as.complex(-5))
#La raiz cuadrada devuelve, delas dos soluciones
#la Positiva para obtener la otra multiplicar por
# (-1)

Z = sqrt(3+2i)*(-1) # = z^2 = 3+2i

#Modulo sqrt(Re(z)^2 + Im(z)^2)

Mod(z1)

#Argumento = arctan(Im(z)/Re(z))
#= arcos(Re(z)/Mod(z))
#= arsin(Im(z)/Re(z))
#va desde (-pi,pi]

Arg(z1) # Arg(-1-2i)

#Conjugado = Re(z)- Im(z)i
Conj(z1)
#Parte real y parte imaginaria
Re(z1)
Im(z1)

### z = Mod(z)*(cos(Arg(z))+sin(Arg(z))i)
complex(modulus = 2,argument = pi/2) -> z2
Mod(z2)
Arg(z2)  #tiene que dar pi/2