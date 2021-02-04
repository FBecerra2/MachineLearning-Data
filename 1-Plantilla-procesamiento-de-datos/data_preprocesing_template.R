#Planilla para el procesamiento de datos

#importar el dataset

dataset = read.csv('Data.csv')
#dataset = dataset[,2:3] Esto es para solo usar columnas 2 y 3 del data set

#Dividir los datos en conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
split = sample.split(dataset$Purchased, SplitRatio = 0.8)
training_set= subset(dataset, split==TRUE)
testing_set= subset(dataset, split==FALSE)

#Escalado de Valores
#training_set[,2:3] = scale(training_set[,2:3])
#testing_set[,2:3] = scale(testing_set[,2:3])