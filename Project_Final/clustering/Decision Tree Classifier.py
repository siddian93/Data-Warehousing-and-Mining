## This File You have to input the Dimesionality of the data You need to generate using the 
# generate_data file imported


import numpy as np
from sklearn import tree
from generate_data import train_data, test_data, train_labels, pred_labels

clf = tree.DecisionTreeClassifier()
clf = clf.fit(train_data, train_labels)

labels_found = clf.predict(test_data)
print labels_found.shape, pred_labels.shape

from sklearn.metrics import accuracy_score
print accuracy_score(pred_labels, labels_found)


#import graphviz 
#dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("Vibrations") 


#import matplotlib.pyplot as plt
#plt.scatter(train_data[:, 0], train_data[:, 1], c = train_labels)
#plt.scatter(test_data[:, 0], test_data[:, 1], c = pred_labels, s = 100)
#plt.scatter(test_data[:, 0], test_data[:, 1], c = labels_found, s = 20)
#plt.show()