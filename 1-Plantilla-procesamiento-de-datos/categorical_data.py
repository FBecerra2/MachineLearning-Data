# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:37:01 2020

@author: Facundo
"""
#Datos Categoricos
#Importar librerias

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar data set
dataset = pd.read_csv("Data.csv")

X =dataset.iloc[:, :-1].values 
###X = dataset.iloc[filas que quiero , columnas que quiero].value
y =dataset.iloc[:, 3].values


# Codificar datos categoricos
from sklearn import preprocessing
le_X = preprocessing.LabelEncoder()
X[:,0] = le_X.fit_transform(X[:,0])
le_y = preprocessing.LabelEncoder()
#Dummyficar la primera columna
###Se usa para que no tome un valor mayot a otro cuando transformamos los datos de letras a numeros
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
ct = ColumnTransformer(
    [('one_hot_encoder', OneHotEncoder(categories='auto'), [0])],   
    remainder='passthrough'                        
)
X = np.array(ct.fit_transform(X), dtype=np.float)

y= np.array(le_y.fit_transform(y), dtype=np.float)

