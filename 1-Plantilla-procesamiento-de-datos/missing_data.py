# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:37:13 2020

@author: Facundo
"""

#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Data.csv")

X =dataset.iloc[:, :-1].values 
###X = dataset.iloc[filas que quiero , columnas que quiero].value
y =dataset.iloc[:, 3].values
#Datos Flatantes

#Tratamientos de NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
###Missing_values = elige el valor a trabajar, strategy =que hacer con ese valor,
imputer = imputer.fit(X[:, 1:3])
###imputer.fit(X) Para arreglar un Objeto con valores nan en columna 1 a 3
X[:, 1:3] = imputer.transform(X[:, 1:3])
###transform devuelve y sustituye les valores NA ver en terminal con X
