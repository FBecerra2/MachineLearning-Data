#c()   define un vector
#scan()  define un vector- se puedo poner un dataseet local o URL entre parentesis
#fix(x)  para modificar visualmente el vector X
#rep(a,n)  para definir un vector constante que contien el dato
#a repetido n veces

rep(1991,10)

#progresion aritmetica
seq(a,b, by = c) 
#ej: ir de 5 a 60 de 5 en 5
#seq(5,60, by = 5)


#empezamso en 4 t terminamo en 35 y tiene que tener 7 saltos
seq(4,35, length.out = 7)
#empieza en 4 tiene que tener 7 saltos de 3 en 3
seq(4, length.out = 7, by = 3)
#pasar una funcion al vector
#sapply(nombre_vector, FUN = nombre de la funcion)
#Ejemplo
#vector x = 1:10
sapply(x, FUN = function(elemento){sqrt(elemento)})

#length(x)= calcula longitud del vector
#max(x)= maximo del vector
#min(x)=minimo del vector
#sum(x)= suma de las entradas del vector
#prod(x)=calcula el producto de las entradas del vector
#mean(x)=calcula la media Aritmetica de las entradas del vector(valor medio)
#diff(x)=camcula el vector formado por la diferencia sucesiva entre
#entradas del vector original.
#comsum(x)=la suma de las entradas de x hasta su posicion (suma el primero ams el segudo y ese resultado con e siguiente)
#

#sort(x) ordena el vector en orden natural
#rev(x) invierte el orden de los elementos del vector x

> vec
[1] 10  0  1 24  1  7 88  5  1  9
> rev(vec)
[1]  9  1  5 88  7  1 24  1  0 10
> sort(rev(vec))
[1]  0  1  1  1  5  7  9 10 24 88
> rev(sort(vec))
[1] 88 24 10  9  7  5  1  1  1  0
> 
  > sort(vec, decreasing = TRUE)
[1] 88 24 10  9  7  5  1  1  1  0

#Sub vectores

x = seq(3,50, by = 3,5)
x
#muestra el 3 vercot
> x[3]
[1] 10
#mustra el ultimo vector
> x[length(x)]
[1] 48.5
#anteultimo vector
> x[length(x)-1]
[1] 45
#muestra solo los vectores del 4 al 8
x[4:8]
#muestra los vectores del 8 al 4
x[8:4]

#muestra numeros grandes
which(x== max(x))


2^pi>pi^2













