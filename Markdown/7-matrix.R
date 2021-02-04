#crear un vector y devolver el que esta en el indice 4
Harry = matrix(-10:27)
Harry[7]   #-4
Harry
#crear una sucesion 0 a 200 y dar e maximo (100*2^n-7*3^n)
n = (0:200)
n
max(100*2^n-7*3^n)   #1499


#Sucesion de 0 a 40 , crear vector 3*5^a-1 y devolverlos
#mayores de 3.5
a = (0:40)
a
b = 3*5^a-1
which(b>3.5)

#funcion que devuelva la parte real, la imaginaria,modulo y argumento
#el conjugado mostrando solo 2 cifras significaticas
info = function(x){print(c(Re(x),Im(x),Mod(x),Arg(x),Conj(x)),2)}
info(2)

#Ecuaciones de segundo grado)(Cuadratica)
solu2 = function(A,B,C){c((-B+sqrt(B^2-4*A*C)/(2*A)),(-B-sqrt(B^2-4*A*C)/(2*A)))}
solu2(4,16,3)

vec = c(0,9,98,2,6,7,5,19,88,20,16,0)
which(vec%%2==0)

