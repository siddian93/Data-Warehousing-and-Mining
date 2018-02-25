import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


ratio  = 0.2
#test, train = load_data(0.2)
data = load_iris().data
cl = load_iris().target
train_set, test_set, cl_train, cl_test  = train_test_split(data, cl, test_size = ratio)
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(train_set, cl_train)
cl_pred = clf.predict(test_set)
print "Accuracy of AdaBoost Ensamble Classifier : ", accuracy_score(cl_pred, cl_test)*100

