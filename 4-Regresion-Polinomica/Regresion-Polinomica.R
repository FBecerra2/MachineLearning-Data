# Regresion polinomica.

#Importar el dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[,2:3]

#Tratamiento de los valores NA
#dataset$Age = ifelse(is.na(dataset$Age),
#                     ave(dataset$Age,FUN = function(x)mean(x,na.rm = TRUE)),
#                     dataset$Age)

#Codificar Variables categoricas
#dataset$Country = factor(dataset$Country,
#                         levels = c("France","Spain","Germany"),
#                         labels = c(1,2,3))

#Dividir los datos en conjunto de entrenamiento y conjunto de test
#set.seed(123)
#split = sample.split(dataset$Purchased, SplitRatio = 0.8)
#training_set= subset(dataset, split==TRUE)
#testing_set= subset(dataset, split==FALSE)

# #Escalado de Valores
# training_set[,2:3] = scale(training_set[,2:3])
# testing_set[,2:3] = scale(testing_set[,2:3])


#Ajustar modelo de regresion linear con el conjunto de datps

lin_reg = lm(formula=Salary ~ .,
             data = dataset)

#Ajustar un modelo de regresion polinomica con el conjunto de Datos
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
poly_reg = lm(formula = Salary ~ .,
              data = dataset)





