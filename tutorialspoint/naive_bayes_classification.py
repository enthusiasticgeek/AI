#!/usr/bin/env python3
import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Naïve Bayes is a classification technique used to build classifier using the Bayes theorem. The assumption is that the predictors are independent. In simple words, it assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature. For building Naïve Bayes classifier we need to use the python library called scikit learn. There are three types of Naïve Bayes models named Gaussian, Multinomial and Bernoulli under scikit learn package.


#dictionary
data = load_breast_cancer()
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']
print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])

#In the example given below, we are using 40 % of the data for testing and the remaining data would be used for training the model.
train, test, train_labels, test_labels = train_test_split(features,labels,test_size = 0.40, random_state = 42)

# Build the model
# Naïve Bayes algorithm
# We use Gaussian subtype from 3 options - Gaussian, Multinomial and Bernoulli under scikit learn package.
gnb = GaussianNB()
model = gnb.fit(train, train_labels)
# Evaluating the model and its accuracy (The series of 0s and 1s are the predicted values for the tumor classes – malignant and benign.)
preds = gnb.predict(test)
print(preds)
print(accuracy_score(test_labels,preds))

