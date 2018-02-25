import numpy as np
import math
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def euclideanDistance(instance1, instance2):
    length = 4
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def find_dist(val):
    dist_mat = []
    for i in xrange(len(val)-1):
        d = []
        for j in xrange(i+1, len(val)):
            d.append(euclideanDistance(val[i], val[j]))
        dist_mat.append( np.asarray(d))
    return dist_mat

def find_dist_average(val):
    dist_mat = []
    for i in xrange(len(val)-1):
        d = []
        c1 = 0.0
        for k in xrange(4):
            c1+=math.pow(val[i][k], 2)
        c1 = math.sqrt(c1)
        for j in xrange(i+1, len(val)):
            c2 = 0.0
            for k in xrange(4):
                c2+=math.pow(val[i][k], 2)
            c2 = math.sqrt(c2)
            d.append((euclideanDistance(val[i], val[j]))/(c1*c2))
        dist_mat.append( np.asarray(d))
    return dist_mat

def find_centroid(val1, val2):
    avg = np.zeros((1, 4))
    for i in xrange(4):
        avg[0][i] = (val1[i] + val2[i])/2 
    return avg

data = load_iris().data
for i in xrange(len(data)-1):
    dist_mat = find_dist(data)
    m=999999999999999999999.0
    for i in xrange(len(dist_mat)):
        if m>min(dist_mat[i]):
            index_j = np.argmin(dist_mat[i])
            index_i = i    
        m = min(m, min(dist_mat[i]))
        
    #print index_j, index_i
    avg_inst = find_centroid(data[index_i], data[index_j])
    data = np.delete(data, index_i, 0)
    data = np.delete(data, index_j, 0)
    data = np.append(data, avg_inst, axis = 0)
    print 'Clusters Merged  -- Single Link : ', index_i, index_j\


data = load_iris().data
for i in xrange(len(data)-1):
    dist_mat = find_dist(data)
    m=-999999999999999999999.0
    for i in xrange(len(dist_mat)):
        if m<max(dist_mat[i]):
            index_j = np.argmax(dist_mat[i])
            index_i = i    
        m = max(m, max(dist_mat[i]))
        
    #print index_j, index_i
    avg_inst = find_centroid(data[index_i], data[index_j])
    data = np.delete(data, index_i, 0)
    data = np.delete(data, index_j, 0)
    data = np.append(data, avg_inst, axis = 0)
    print 'Clusters Merged  -- Double Link : ', index_i, index_j\


data = load_iris().data
for i in xrange(len(data)-1):
    dist_mat = find_dist_average(data)
    m=999999999999999999999.0
    for i in xrange(len(dist_mat)):
        if m>min(dist_mat[i]):
            index_j = np.argmin(dist_mat[i])
            index_i = i    
        m = min(m, min(dist_mat[i]))
        
    #print index_j, index_i
    avg_inst = find_centroid(data[index_i], data[index_j])
    data = np.delete(data, index_i, 0)
    data = np.delete(data, index_j, 0)
    data = np.append(data, avg_inst, axis = 0)
    print 'Clusters Merged  -- Average Link : ', index_i, index_j


