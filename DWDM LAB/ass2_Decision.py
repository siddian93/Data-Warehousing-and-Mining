#!usr/bin/env python

import graphviz
from sklearn import tree
from sklearn.datasets import load_iris

data = load_iris()
print data.data
#print data.data, data.target
clf = tree.DecisionTreeClassifier().fit(data.data, data.target)
#dot_data = tree.export_graphviz(clf, out_file=None) 
#graph = graphviz.Source(dot_data) 
#graph.render("iris")
dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=data.feature_names,  
                         class_names=data.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True) 
graph = graphviz.Source(dot_data)
graph.view()