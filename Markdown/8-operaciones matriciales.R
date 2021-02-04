#Funcion apply
#Operaciones de las matrices

t(matriz)  = transpuesta de la matriz

+  = sumaar matrices matrices
* = producto de un escalar por una matriz
%*%= multiplicar matrices

mtx.exp(matriz,n) = elevar la matriz a n
%%= elevar matrices

No las eleven exactamente sino que las aproxima


M = matrix(1:12, nrow = 4)
M

t(M)
M%*%t(M)

A = rbind(c(2,0,2),c(1,2,3),c(0,1,3))
A
B = rbind(c(3,2,1), c(1,0,0),c(1,1,1))
B

A%*%B
B%*%A
A%*%A
B%*%B%*%B


det(matriz) = determinante de la matriz
qr(matriz)$rank = rango de la matriz
solve(matriz) = inversa de una matriz invertible
solve=(matriz,b) = 

  
qr(M)$rank
solve(M)

M = rbind(c(1,4,2),c(0,1,3),c(1,8,9))
qr(M)$rank
solve(M)
solve(M)%*%M
round(solve(M)%*%M)

solve(M,c(1,2,3))


#vector propio , valor propio

eigen(matriz)= calcular valores(vaps) y vectore propios(veps)
-eigen(matriz)$values = da el vector con los vaps de la matriz en orden decreciente
de su valor absoluto.
-eigen(matriz)$vectors = da una matriz cuyas columnas don los
veps de la matriz

eigen(M)
eigen(M)$values
eigen(M)$vectors






