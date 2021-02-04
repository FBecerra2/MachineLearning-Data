#Planilla para el procesamiento de datos

#importar el dataset

dataset = read.csv('Curso/Machine Learning/2-Regresion-Lineal/Salary_Data.csv')
#dataset = dataset[,2:3] Esto es para solo usar columnas 2 y 3 del data set

#Dividir los datos en conjunto de entrenamiento y conjunto de test
library(caTools)
set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set= subset(dataset, split==TRUE)
testing_set= subset(dataset, split==FALSE)

#Escalado de Valores
#training_set[,2:3] = scale(training_set[,2:3])
#testing_set[,2:3] = scale(testing_set[,2:3])

#Ajustar el modelo de Regresion 
#lineal simple con el conjunto de entrenamineto

regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set) #lm crea un modelo lineal

#Predecir resultados con el conjunto de test

y_pred = predict(regressor, newdata = testing_set) 
#tiene que tener los mismo nombres en las columnas igual a el conjunto de entrenamiento

#Visualizacion de los resultados en el conjunto de entrenamiento
#Graficos para ver que tan bien se ajustan los datos de la prediccion
library(ggplot2)
ggplot() + 
  geom_point(aes(x = training_set$YearsExperience, y = training_set$Salary),
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience,
                y = predict(regressor, newdata = training_set)),
            colour ="blue") +
  ggtitle("Sueldo vs Años de experiencia ((Conjunto de Entrenamiento))") +
  xlab("Años de Experiencia") +
  ylab("Sueldo (en $)")


#Visualizacion de los resultados en el conjunto de testing

ggplot() + 
  geom_point(aes(x = testing_set$YearsExperience, y = testing_set$Salary),
             colour = "red") +
  geom_line(aes(x = training_set$YearsExperience,
                y = predict(regressor, newdata = training_set)),
            colour ="blue") +
  ggtitle("Sueldo vs Años de experiencia ((Conjunto de Testing))") +
  xlab("Años de Experiencia") +
  ylab("Sueldo (en $)")

