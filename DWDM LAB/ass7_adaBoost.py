import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

def load_data(ratio):
    data = load_iris().data
    cl = load_iris().target
    train_set, test_set, cl_train, cl_test  = train_test_split(data, cl, test_size = ratio)
    #train_data, test_data = [] , []
    train_data = np.zeros((len(train_set), 5))
    test_data = np.zeros((len(test_set), 5))
    #print train_data
    for i in range(len(train_set)):
        for j in range (4):
            train_data[i][j] = train_set[i][j]
        train_data[i][4] = cl_train[i]

    for i in range(len(test_set)):
        for j in range (4):
            test_data[i][j] = test_set[i][j]
        test_data[i][4] = cl_test[i]

    return test_data, train_data


ratio  = 0.2
#test, train = load_data(0.2)
data = load_iris().data
cl = load_iris().target
train_set, test_set, cl_train, cl_test  = train_test_split(data, cl, test_size = ratio)
#print cl_train
clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=1), algorithm="SAMME", n_estimators=200)
clf.fit(train_set, cl_train)
cl_pred  = clf.predict(test_set)
#print cl_pred
print "Accuracy of AdaBoost Ensamble Classifier : ", accuracy_score(cl_pred, cl_test)*100