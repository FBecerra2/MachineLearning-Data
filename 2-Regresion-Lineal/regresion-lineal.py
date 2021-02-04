# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:40:05 2020

@author: Facundo
"""

##Regrasion Lineal Simple
#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Salary_Data.csv")

X =dataset.iloc[:, :-1].values 
###X = dataset.iloc[filas que quiero , columnas que quiero].value
y =dataset.iloc[:, 1].values

#Dividir el Dataet en  conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0) #random state es la semilla


#Escalado de Variable En REGRESION LINEAL SIMPLE NO HACE FALTA
 #from sklearn import preprocessing  
"""#---- Esto es a veces pero es de uso 
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Crear modelo de Regrasion lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train,y_train)

#Predecir el conjunto de test
y_pred = regression.predict(X_test)

#Visulizar los resultados de entrenamiento
plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regression.predict(X_train))
plt.title("Sueldo vs Años de Experiencias (Conjunro de entrenamiento)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo en $")
plt.show()

#Visualizar los resultados de test
plt.scatter(X_test,y_test,color="red")
plt.plot(X_train,regression.predict(X_train))
plt.title("Sueldo vs Años de Experiencias (Conjunto de Test)")
plt.xlabel("Años de experiencia")
plt.ylabel("Sueldo en $")
plt.show()




