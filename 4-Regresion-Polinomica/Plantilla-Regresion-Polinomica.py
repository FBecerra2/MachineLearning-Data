# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 20:11:48 2020

@author: Facundo
"""

#plantilla de Regresion

#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Position_Salaries.csv")
X =dataset.iloc[:, 1:2].values 
y =dataset.iloc[:, 2].values

#Dividir Dataset en test y train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(0.2), random_state=0)

#Escalado de Variable
 #from sklearn import preprocessing  
"""#---- Esto es a veces pero es de uso 
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Ajustar la regresion con el dataset
# lineal polinomico o el que sea

DEFINIR ACA REGGRESION

#Prediccion de nuestros modelos
y_pred=regression.predict([[6.5]])



#visualizacion de los resultados del modelo polinomico
X_grid = np.arange(min(X) , max(X) , 0.1)
X_grid = X_grid.reshape(len(X_grid), 1)
#Suavizar la linea
plt.scatter(X, y , color="red")
plt.plot(X_grid, reggresion.predict(X_grid),color="blue")
#plt.plot(X, lin_reg_2.predict(X_poly),color="blue")
plt.title("Modelo de regresion")
plt.xlabel("Posicion empleado")
plt.ylabel("Sueldo en $")
plt.show()
