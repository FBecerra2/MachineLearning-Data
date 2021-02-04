# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 15:41:51 2020

@author: Facundo
"""


# Regresion Polinomica

#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Position_Salaries.csv")

X =dataset.iloc[:, 1:2].values #1:2 lo convierte en matriz
###X = dataset.iloc[filas que quiero , columnas que quiero].values

y =dataset.iloc[:, 2].values

#Dividir el Dataset en  conjunto de entrenamiento y conjunto de testing
#from sklearn.model_selection import train_test_split
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(0.2), random_state=0) #random state es la semilla


#Escalado de Variable
 #from sklearn import preprocessing  
"""#---- Esto es a veces pero es de uso 
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Ajustar la regresion lineal con el dataset

from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(X,y)

#Ajustas la regresion polinomica con el dataset
from sklearn.preprocessing import PolynomialFeatures
poly_reg = PolynomialFeatures(degree=4)
#el primer parametro es hasta que grado quiero tener

#fit_transform crea el modelo y lo transforma (Actualiza)
X_poly=poly_reg.fit_transform(X)
lin_reg_2=LinearRegression()
lin_reg_2.fit(X_poly, y)

#visualizacion de los resultados de Modelo Lineal

plt.scatter(X, y , color="red")
plt.plot(X, lin_reg.predict(X),color="blue")
plt.title("Modelo de regresion lineal")
plt.xlabel("Posicion empleado")
plt.ylabel("Sueldo en $")
plt.show()

#visualizacion de los resultados del modelo polinomico
X_grid = np.arange(min(X) , max(X) , 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
#Suavizar la linea
plt.scatter(X, y , color="red")
plt.plot(X_grid, lin_reg_2.predict(poly_reg.fit_transform(X_grid)),color="blue")
#plt.plot(X, lin_reg_2.predict(X_poly),color="blue")
plt.title("Modelo de regresion polinomica")
plt.xlabel("Posicion empleado")
plt.ylabel("Sueldo en $")
plt.show()

#Prediccion de nuestros modelos
lin_reg.predict([[6.5]])
lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))


