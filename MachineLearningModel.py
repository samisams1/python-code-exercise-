from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3]])
y = np.array([3, 5, 7])

model = LinearRegression()
model.fit(X, y)

print(model.predict([[4]]))