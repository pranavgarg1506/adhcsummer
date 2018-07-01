#!/usr/bin/python3

from sklearn import datasets
data = datasets.load_boston()
import numpy as np
import pandas as pd
import statsmodels.api as sm

df = pd.DataFrame(data.data, columns=data.feature_names)
target = pd.DataFrame(data.target, columns=["MEDV"])


X = df["RM"]
y = target["MEDV"]

model = sm.OLS(y, X).fit()
predictions = model.predict(X)

print(model.summary())
