#!usr/bin/env python

import math
from random import random
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)


data = load_iris().data
cl = load_iris().target
train_set, test_set, cl_train, cl_test  = train_test_split(data, cl, test_size = 0.2)

train_data, test_data = [], []
train_class = []
for i in range(len(train_set)):
    train_data.append(list(train_set[i]))
    train_data[i].append(cl_train[i])
    

for i in range(len(test_set)):
    test_data.append(list(test_set[i]))
    test_data[i].append(cl_test[i])

#print train_data[0]

S = []
S.append(train_data[0])
del train_data[0]

for x in train_data:
    dist = []
    for y in S:
        dist.append(euclideanDistance(x, y, 4))
        
    index = dist.index(min(dist))
    if x[4] != S[index][4]:
        S.append(x) 


## Modified CNN
G = []
G = [1]
count = 0
while(G != []):
    G = []
    f1, f2, f3 = 0, 0, 0
    for x in test_data:
        dist = []
        for y in S:
            dist.append(euclideanDistance(x, y, 4))
        index = dist.index(min(dist))
        #print index
        #print S[index][4]
        #print x[4]
        if x[4] != S[index][4]:
            G.append(x)
        if G != [] :
            for p in G:
                #print 'Dude', p
                if p[4] == 1 and f1 == 0 :
                    S.append(p)
                    f1 = 1
                if p[4] == 2 and f2 == 0:
                    S.append(p)
                    f2 = 1
                if p[4] == 3 and f3 == 0:
                    S.append(p)
                    f3 = 1
    count+=1
    if count>10:
        break
    
accuracy = (1-float(len(G))/len(test_data))*100 
print accuracy