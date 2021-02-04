#LIstas Generalizadas

x=c(1,5,-2,6,-7,8,-3,4,-9)

L = list(nombre = "temperaturas", datos=x , media=mean(x), sumas=cumsum(x))

L

L$media
L$datos
L$nombre
L[[3]]
L[[2]]

3*L[[2]]

#Funciones de una Lista

str(list)
names(list)

names(L)
str(L)

summary(lm(c(1,2,3,4)~c(1,2,3,6)))
reg <-lm(c(1,2,3,4)~c(1,2,3,6))
reg$coefficients