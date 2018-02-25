#!usr/bin/env python

import math
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def euclideanDistance(instance1, instance2):
    length = 4
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

data = load_iris().data
cl = load_iris().target
train_set, test_set, cl_train, cl_test  = train_test_split(data, cl, test_size = 0.2)

train_data, test_data = [], []
for i in range(len(train_set)):
    train_data.append(list(train_set[i]))
    train_data[i].append(cl_train[i])
    

for i in range(len(test_set)):
    test_data.append(list(test_set[i]))
    test_data[i].append(cl_test[i])

dist = []
count = 0
for x in test_data:
    for y in train_data:
        dist.append(euclideanDistance(x, y));
    i = dist.index(min(dist))
    if (x[4] != train_data[i][4]):
        count +=1        


print 'Accuracy: ', (1-float(count)/len(test_data))*100,  '%'
#print 'Classified Class :', cl[d.index(min(d))], 'Actual Class: ', test_set_class   

