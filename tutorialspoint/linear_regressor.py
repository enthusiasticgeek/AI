#!/usr/bin/env python3

import numpy as np
from sklearn import linear_model
import sklearn.metrics as sm
import matplotlib.pyplot as plt

input = './linear.txt'

#load the data
input_data = np.loadtxt(input, delimiter=',')
print(input_data)
X, y = input_data[:, :-1], input_data[:, -1]

#train the model
training_samples = int(0.6 * len(X))
#testing_samples = len(X) - num_training
testing_samples = len(X) - training_samples

X_train, y_train = X[:training_samples], y[:training_samples]

X_test, y_test = X[training_samples:], y[training_samples:]

#linear regressor object
reg_linear = linear_model.LinearRegression()

#Train the object with the training samples.
reg_linear.fit(X_train, y_train)

#predict with test data
y_test_pred = reg_linear.predict(X_test)

#plot and visualize
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_test, y_test_pred, color = 'black', linewidth = 2)
plt.xticks(())
plt.yticks(())
plt.show()
