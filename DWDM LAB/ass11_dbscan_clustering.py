import numpy as np
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def find_neighbour(data, index, eps):
    neighbors = []
    
    for i in range(len(data)):
        if np.linalg.norm(data[index] - data[i]) < eps:
           neighbors.append(i)
            
    return neighbors

def add_to_cluster(data, labels, index, neighbors_of_i, c_id, eps, min_points):
    labels[index]  = c_id
    i = 0
    
    while i< len(neighbors_of_i):
        P_next = neighbors_of_i[i]
        #print P_next
        if labels[P_next] == -1:
            labels[P_next] = c_id
        elif labels[P_next] == 0:
            labels[P_next] = c_id
            neighbour  = find_neighbour(data, P_next, eps)
            if len(neighbour) >= min_points:
                neighbors_of_i = neighbors_of_i + neighbour
        i+=1
    #print labels    


def find_border_points():
    ### Find the Border Points from here  

def DBSCAN(data, eps, min_points):
    labels = np.zeros(len(data), dtype=np.int)
    c_id  = 0
    neighbors_of_i = []
    core_points = []
    for i in xrange(len(data)):
        if ~(labels[i] == 0):
            continue
        neighbors_of_i  = find_neighbour(data, i, eps)
        if len(neighbors_of_i) < min_points:
            labels[i] = -1
        else :
            core_points.append(i)
            c_id+=1
            add_to_cluster(data, labels, i, neighbors_of_i, c_id, eps, min_points)
    return labels, core_points

data = load_iris().data
labels = load_iris().target
#print labels
eps = 0.4
min_points  = 3
labels, core_points = DBSCAN(data, eps, min_points)
print core_points
border_points = find_border_points(data, core_points, eps, min_points)
print border_points