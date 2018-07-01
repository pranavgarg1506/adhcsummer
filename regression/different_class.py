#!/usr/bin/python3

import numpy as np
import pandas as pd
from  sklearn import  datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier


data = pd.read_csv('Housing.csv')

x_train,x_text,y_train,y_test = train_test_split(data['price'],data['lotsize'],test_size=0.3)

print(type(x_train))
print(type(x_text))
print(type(y_train))
print(type(y_test))

'''
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)
knn.predict(x_test)
print("KNeighborsClassifier: "+str(knn.score(x_test, y_test)))


'''
