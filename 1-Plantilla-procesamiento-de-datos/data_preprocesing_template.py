# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:41:46 2020

@author: Facundo
"""


#Plantilla standard


#Plantilla de Preprocesado

#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Data.csv")

X =dataset.iloc[:, :-1].values 
###X = dataset.iloc[filas que quiero , columnas que quiero].value
y =dataset.iloc[:, 3].values

#Dividir el Dataet en  conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(0.2), random_state=0) #random state es la semilla


#Escalado de Variable
 #from sklearn import preprocessing  
"""#---- Esto es a veces pero es de uso 
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)"""