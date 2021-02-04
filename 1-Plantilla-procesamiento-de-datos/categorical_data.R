#Planilla para el procesamiento de datos - Datos Categoricos
#importar el dataset

dataset = read.csv('Data.csv')

#Codificar Variables categoricas

dataset$Country = factor(dataset$Country,
                         levels = c("France","Spain","Germany"),
                         labels = c(1,2,3))

dataset$Purchased = factor(dataset$Purchased,
                           levels = c("No","Yes"),
                           labels = c(0,1))