import math
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

############## Load IRIS and Disect Data to TEST and TRAIN sets ####################
########## Class information is now a part of the feature vector ###################
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

############### Modified Test Data ####################################
'''
test_data[0:3] is the feature and test_data[:, 4] is the class label
same goes for train_data
'''

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
	return math.sqrt(distance)

def find_KNN(k, test, train):
    #print test[0][: 4], train[0][: 4]
    label = np.zeros((len(test), 1))
    #print label
    for i in range(len(test)):
        dist = []
        for j in range (len(train)):
            d = euclideanDistance(test[i][: 4], train[j][: 4], 4)
            dist.append([d, train[j][4]])
        dist.sort()
        dist= dist[:k]
        cl = []
        for i in range(len(dist)):
            cl.append(dist[i][1])
        mode = Counter(cl)
        #print mode.most_common(1)[0][0]
        label[i][0] = mode.most_common(1)[0][0]
        #print len(dist)
    return label

def error_in_classification(label, test):
    e = 0
    for i in range(len(test)):
        if test[i][4] != label[i][0]:
            e+=1
    #e_perc = 0.0
    e_perc = (float(e)/len(test))*100
    #print e_perc
    return e_perc


test, train = load_data(0.2)
k = 5;
error = []
for i in range(1, 11):
    label = find_KNN(i, test, train)
    error.append(error_in_classification(label, test))
#print len(train), len(test)
min_err = min(error)
opt_k = 0
for i in range(len(error)):
    if (min_err == error[i]):
        opt_k = i+1
        break
print 'Accuracy Weighted KNN: ', 100-min_err, 'Optimal K = ', opt_k
#plt.plot(error)
#plt.show()