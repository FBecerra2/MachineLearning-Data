# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 01:00:23 2020

@author: Facundo
"""
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv("Data.csv")
print(dataset)
X =dataset.iloc[:, :-1].values 
y =dataset.iloc[:, 1].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) #random state es la semilla
print(X_train)
print(X_test)
print()
print(y_train)
print(y_test)


from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(X_train,y_train)

plt.scatter(X_train,y_train,color="red")
plt.plot(X_train,regression.predict(X_train))
plt.title("Dinero invertido (Conjunyo de entrenamiento)")
plt.xlabel("Gastos")
plt.ylabel("Ingresos")
plt.show()

plt.scatter(X_test,y_test,color="red")
plt.plot(X_train,regression.predict(X_train))
plt.title("Dinero invertido (Conjunyo de test)")
plt.xlabel("Gastos")
plt.ylabel("Ingresos")
plt.show()

