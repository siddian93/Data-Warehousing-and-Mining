import numpy as np
import math
import matplotlib.pyplot as plt
from collections import Counter
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def euclideanDistance(instance1, instance2):
    length = 4
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

class cluster_mean:
    instances = []
    
    def __init__(self):
        self.instances = []
        #print 'New Cluster Innitialized'
    
    def mean(self):
        s = 0.0
        m_c = []
        for j in range(4):
            s = 0.0
            for i in range(len(self.instances)):
                s+=self.instances[i][j]
            m_c.append(s/len(self.instances))                
        m_c = (["%.2f" % elem for elem in m_c])
        m_c = [float(i)  for i in m_c]
        return m_c
    
    def add_to_cluster(self, instance):
        self.instances.append(instance)

'''
d_set = load_iris().data
cl = load_iris().target
k = 3
data = np.zeros((len(d_set), 5))
for i in range(len(d_set)):
    data[i][:4] = d_set[i]
    data[i][4]  = cl[i] 


class1, class2, class3 = [], [], [] 
prev_m1, prev_m2, prev_m3 = 0.0, 0.0, 0.0 
m1, m2, m3 = 1, 1, 1
cl1 = cluster_mean()
cl2 = cluster_mean()
cl3 = cluster_mean()
cl1.add_to_cluster(data[0])
cl2.add_to_cluster(data[51])
cl3.add_to_cluster(data[101])
while(prev_m1 != m1 and prev_m2 != m2 and prev_m3 != m3):
    m1, m2, m3 = cl1.mean(), cl2.mean(), cl3.mean()
    for x in data:
        f1 = euclideanDistance(x, m1);
        f2 = euclideanDistance(x, m2);
        f3 = euclideanDistance(x, m3);
        d = min(f1, f2, f3)
        if d == f1:
            cl1.add_to_cluster(x)
        elif d == f2:
            cl2.add_to_cluster(x)
        elif d == f3:
            cl3.add_to_cluster(x)
    
    prev_m1, prev_m2, prev_m3 = m1, m2, m3
    m1, m2, m3 = cl1.mean(), cl2.mean(), cl3.mean()
class1, class2, class3 = cl1.instances, cl2.instances, cl3.instances


class1 = np.asarray(class1)
class2 = np.asarray(class2)
class3 = np.asarray(class3)

cluster = []
cluster.append(class1)
cluster.append(class2)
cluster.append(class3)

error = 0.0
for x in class1:
    if x[4]!=0:
        error+=1

for x in class2:
    if x[4]!=1:
        error+=1

for x in class3:
    if x[4]!=2:
        error+=1

center = []
center.append(data[0])
center.append(data[51])
center.append(data[101])

sse = 0

for x in class1:
     v1 = math.pow((center[0][0] - x[0]), 2)
     v2 = math.pow((center[0][1] - x[1]), 2)
     v3 = math.pow((center[0][2] - x[2]), 2)
     v4 = math.pow((center[0][3] - x[3]), 2)
     sse += v1+v2+v3+v4

for x in class2:
     v1 = math.pow((center[1][0] - x[0]), 2)
     v2 = math.pow((center[1][1] - x[1]), 2)
     v3 = math.pow((center[1][2] - x[2]), 2)
     v4 = math.pow((center[1][3] - x[3]), 2)
     sse += v1+v2+v3+v4

for x in class3:
     v1 = math.pow((center[2][0] - x[0]), 2)
     v2 = math.pow((center[2][1] - x[1]), 2)
     v3 = math.pow((center[2][2] - x[2]), 2)
     v4 = math.pow((center[2][3] - x[3]), 2)
     sse += v1+v2+v3+v4
sse = math.sqrt(sse)

print "SSE of the CLustring is : ", sse
'''
data = load_iris().data
k = 2
clf = KMeans(n_clusters=k)
clf.fit(data)
cluster = [[], [], []]
for i in xrange(len(data)):
    cluster[clf.labels_[i]].append(data[i])

while(len(cluster)<6):
    clus = np.asarray(cluster[0])
    cluster.pop(0)
    min_sse1, min_sse2 = 9999999999999.0, 9999999999999.0 
    for  i in xrange(1):
        for j in xrange(len(clus)):
            for k in xrange(len(clus)):
                if i == k:
                    continue
                cl1 = cluster_mean()
                cl2 = cluster_mean()
                cl1.add_to_cluster(clus[i])
                cl2.add_to_cluster(clus[j])
                m1 = cl1.mean()
                m2 = cl2.mean()
                for x in clus:
                    f1 = euclideanDistance(x, m1);
                    f2 = euclideanDistance(x, m2);
                    d = min(f1, f2)
                    if d == f1:
                        cl1.add_to_cluster(x)
                    else:
                        cl2.add_to_cluster(x)
                class1 = np.asarray(cl1.instances)
                class2 = np.asarray(cl2.instances)
                
                acc_clus1 = class1
                acc_clus2 = class2
                sse = 0

                for x in class1:
                    v1 = math.pow((clus[i][0] - x[0]), 2)
                    v2 = math.pow((clus[i][1] - x[1]), 2)
                    v3 = math.pow((clus[i][2] - x[2]), 2)
                    v4 = math.pow((clus[i][3] - x[3]), 2)
                    sse = v1+v2+v3+v4
                sse1 = math.sqrt(sse)
                sse = 0
                for x in class2:
                    v1 = math.pow((clus[j][0] - x[0]), 2)
                    v2 = math.pow((clus[j][1] - x[1]), 2)
                    v3 = math.pow((clus[j][2] - x[2]), 2)
                    v4 = math.pow((clus[j][3] - x[3]), 2)
                    sse = v1+v2+v3+v4
                sse2 = math.sqrt(sse)

                d = min(sse1, sse2)
                if d == sse1:
                    if min_sse1 > d:
                        acc_clus1 = class1
                if d  == sse2:
                    if min_sse2 > d:
                        acc_clus2 = class2
                        
    cluster.append(acc_clus1)
    cluster.append(acc_clus2)
print 'Total Number of Clusters Formed : ', len(cluster)
print cluster[0]
print cluster[1]
print cluster[2]
print cluster[3]
print cluster[4]
print cluster[5]

