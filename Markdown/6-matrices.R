## Matrices

matrix(vector, nrow = n (numero de filas), byrow =x (si se iguala a TRUE se construye por columnas))

M = matrix(1:12, nrow = 4)
M
M = matrix(1:12, nrow = 3)
M
M = matrix(1:12, nrow = 5)
M
M = matrix(1, nrow = 4,ncol=6)
M
x=0
M = matrix(4:20, nrow = 3,ncol=5)
M
M = matrix(1:12, nrow = 5,ncol=3)

#rbind(vertor1,vector2)
#cbind(vertor1,vector2)
#diag(vector)
rbind(M, c(1,2,3),c(-1,-2,-3))  #agrega filas a la matriz
rbind(c(1,2,3),c(-1,-2,-3))    #crea matrices en filas
cbind(c(1,2,3),c(-1,-2,-3))   # crea matriz por columna
diag(c(1,2,3,4))             #Crea una diagon con numero 1,2,3,4
diag(5, nrow = 3)


M[2,3]
M[2, ]
M[ ,3]
M[c(2,3,5), 1:2] # sub matriz

#diag(matriz) obtiene la diagonal de la matriz
#nrow(matriz) da el nuemro de filas de la matriz
#ncol(matriz) da el numero de columnas de la matriz
#dim(matriz) dimensiones d ela matriz
#sum(matriz) suma de todas las entradas de la matriz
#prod(matriz) producto de las entrada de la matriz
#mean(matriz) media aritmetica de la matriz
#colSums(matriz) suma por columnas de la matriz
#rowSum(matriz) suma por filas de la matriz
#rowMeans(matriz) media aritmetica de las filas
#colMeans(matriz) media aritmetica de las columnas

#Cuadrado de cada una de las entradas de la matriz
apply(M, MARGIN = 1, FUN = function(x){x^2})









