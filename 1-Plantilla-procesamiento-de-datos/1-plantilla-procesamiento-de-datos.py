# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 14:15:26 2020

@author: Facundo
"""


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

#Tratamientos de NAs
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
###Missing_values = elige el valor a trabajar, strategy =que hacer con ese valor,
imputer = imputer.fit(X[:, 1:3])
###imputer.fit(X) Para arreglar un Objeto con valores nan en columna 1 a 3
X[:, 1:3] = imputer.transform(X[:, 1:3])
###transform devuelve y sustituye les valores NA ver en terminal con X


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

#Dividir el Dataet en  conjunto de entrenamiento y conjunto de testing

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=(0.2), random_state=0) #random state es la semilla

#Escalado de Variable
 #from sklearn import preprocessing
sc_X = preprocessing.StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)
