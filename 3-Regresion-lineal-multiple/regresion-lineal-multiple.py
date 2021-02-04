# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 00:26:34 2020

@author: Facundo
"""
# Regresion lineal multiple

#Plantilla de Preprocesado

#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("50_Startups.csv")
X =dataset.iloc[:, :-1].values
y =dataset.iloc[:, 4].values

# Codificar datos categoricos
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

le_X = preprocessing.LabelEncoder()
X[:,3] = le_X.fit_transform(X[:,3])

ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [3])],   
    remainder='passthrough'                        
)
X = np.array(ct.fit_transform(X), dtype=np.float)

#Evitar la trampa de las variables ficticias(Si tengo 3 variables solo debo
#quedarme con dos variables DUMMY "Abajo elimino la primera columna")
X=X[:, 1:]

#Dividir el Dataset en  conjunto de entrenamiento y conjunto de testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(0.2), random_state=0) #random state es la semilla


#Escalado de Variable
 #from sklearn import preprocessing  
"""#---- Esto es a veces pero es de uso 
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""

#Ajustar el modelo de regresion lineal multiple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train, y_train)

#Prediccion de los resultados en el conjunto de testing
y_pred=regression.predict(X_test)

#Construuir el modelo optimod e regresion lienal multiple
#utilizando la Eliminacion Hacia atras
import statsmodels.api as sm
# np.append agrega en fila o columna,agrega un arr = array 
#a X con valores 1 en 50 filas 1ra columna y lo convierte a entero 
#axis indica, 0 fila - 1 columna (Agrega al final)
##Con esto se agraga el termino independiente Y con todos 1
X = np.append(arr = np.ones((50,1)).astype(int), values=X,axis=1)

#variable que guarda el modelo optimo (Guarda los valores 
#estadisticamente significativos para predecir la Y)
X_opt= X[:,[0,1,2,3,4,5]]
SL = 0.05
#creamos una variable nueva y pasamos los datos originales con
#los np.ones en las variables endogenas y exogenas
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
#Devuelve p_valor , coeficientes y modelos
regression_OLS.summary()

X_opt= X[:,[0,1,3,4,5]]
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
regression_OLS.summary()

X_opt= X[:,[0,1,4,5]]
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
regression_OLS.summary()

X_opt= X[:,[0,3,4,5]]
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
regression_OLS.summary()

X_opt= X[:,[0,3,5]]
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
regression_OLS.summary()

X_opt= X[:,[0,3]]
regression_OLS=sm.OLS(endog = y, exog= X_opt).fit()
regression_OLS.summary()

#Eliminación hacia atrás utilizando  p-valores y el valor de  R Cuadrado Ajustado:

import statsmodels.formula.api as sm
def backwardElimination(x, SL):    
    numVars = len(x[0])    
    temp = np.zeros((50,6)).astype(int)    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        adjR_before = regressor_OLS.rsquared_adj.astype(float)        
        if maxVar > SL:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    temp[:,j] = x[:, j]                    
                    x = np.delete(x, j, 1)                    
                    tmp_regressor = sm.OLS(y, x.tolist()).fit()                    
                    adjR_after = tmp_regressor.rsquared_adj.astype(float)                    
                    if (adjR_before >= adjR_after):                        
                        x_rollback = np.hstack((x, temp[:,[0,j]]))                        
                        x_rollback = np.delete(x_rollback, j, 1)     
                        print (regressor_OLS.summary())                        
                        return x_rollback                    
                    else:                        
                        continue    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)


#Eliminación hacia atrás utilizando solamente p-valores:

import statsmodels.formula.api as sm
def backwardElimination(x, sl):    
    numVars = len(x[0])    
    for i in range(0, numVars):        
        regressor_OLS = sm.OLS(y, x.tolist()).fit()        
        maxVar = max(regressor_OLS.pvalues).astype(float)        
        if maxVar > sl:            
            for j in range(0, numVars - i):                
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):                    
                    x = np.delete(x, j, 1)    
    regressor_OLS.summary()    
    return x 
 
SL = 0.05
X_opt = X[:, [0, 1, 2, 3, 4, 5]]
X_Modeled = backwardElimination(X_opt, SL)