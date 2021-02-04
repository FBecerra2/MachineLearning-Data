# Regresion lineal multiple

#Planilla para el procesamiento de datos

#importar el dataset

dataset = read.csv('50_Startups.csv')
#dataset = dataset[,2:3] Esto es para solo usar columnas 2 y 3 del data set

#Codificar Variables categoricas

dataset$State = factor(dataset$State,
                         levels = c("New York","California","Florida"),
                         labels = c(1,2,3))

#Dividir los datos en conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set= subset(dataset, split==TRUE)
testing_set= subset(dataset, split==FALSE)

#Escalado de Valores - Estoes cuando se especifica la escala
#training_set[,2:3] = scale(training_set[,2:3])
#testing_set[,2:3] = scale(testing_set[,2:3])

#Ajustar el modelo de regresion lineal multiple con el
#Conjunto de Entrenamiento
regression = lm(formula = Profit ~ .,
                data = training_set)
#con el punto toma todas las columnas que sobran
# lm(formula = y ~ x)

#Predecir los resultados con el conjunto de testing
y_pred= predict(regression, newdata = testing_set)

#Construir un modelo optimo ocn la eliminacion Hacia atras
#Aca estan todas las variables
SL = 0.05
regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State ,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend ,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend + Marketing.Spend ,
                data = dataset)
summary(regression)

regression = lm(formula = Profit ~ R.D.Spend ,
                data = dataset)
summary(regression)

#Regresion hacia tras multple R

backwardElimination <- function(x, sl) {
  numVars = length(x)
  for (i in c(1:numVars)){
    regressor = lm(formula = Profit ~ ., data = x)
    maxVar = max(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"])
    if (maxVar > sl){
      j = which(coef(summary(regressor))[c(2:numVars), "Pr(>|t|)"] == maxVar)
      x = x[, -j]
    }
    numVars = numVars - 1
  }
  return(summary(regressor))
}

SL = 0.05
dataset = dataset[, c(1,2,3,4,5)]
backwardElimination(training_set, SL)




