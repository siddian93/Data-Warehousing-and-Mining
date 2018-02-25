import csv
import numpy as np 
import pyexcel as pe
from openpyxl import load_workbook
from sklearn.cluster import MeanShift, estimate_bandwidth, DBSCAN

def normalize(sensor):
    means = np.mean(sensor, axis=0)
    l, w = sensor.shape
    for j in xrange(w):
        for i in xrange(l):
            if sensor[i][j] == 0:
                sensor[i][j] = means[j]
    return sensor

data_temp, data  = [], []
sheet = pe.get_sheet(file_name='KitCat.xlsx')
for record in sheet:
    data_temp.append(record)

for i in range(1, len(data_temp)):
    for j in range(9):
        data_temp[i].remove('')
    data.append(data_temp[i])   

sensor1 = []
sensor2 = []

for i in range(len(data)-1):
    if i%2  == 1:
        sensor1.append(data[i][1:7])
    else :
        sensor2.append(data[i][1:7])
sensor1.append(data[i+1][1:7])
sensor1 = np.array(sensor1, dtype=float)
sensor2 = np.array(sensor2, dtype=float)
#sensor1 = np.append(sensor1, sensor2, axis = 0)
#print len(sensor1)
sensor1_attributes = data_temp[0][1:7]
sensor2_attributes = data_temp[0][9:16]
#print sensor1_attributes 
#print sensor2_attributes 

sensor1 = normalize(sensor1)
sensor2 = normalize(sensor2)

clf  = DBSCAN(eps=0.2, min_samples=5)
clf.fit(sensor1)
labels = clf.labels_
core_samples_mask = np.zeros_like(clf.labels_, dtype=bool)
labels_unique = np.unique(labels)
print len(labels)
n_clusters_ = len(labels_unique)
print n_clusters_

# Plot result
import matplotlib.pyplot as plt

colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(labels_unique))]
for k, col in zip(labels_unique, colors):
    #if k == -1:
        # Black used for noise.
    #    col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = sensor1[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = sensor1[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


clf  = DBSCAN(eps=0.2, min_samples=5)
clf.fit(sensor2)
labels = clf.labels_
core_samples_mask = np.zeros_like(clf.labels_, dtype=bool)
labels_unique = np.unique(labels)
print len(labels)
n_clusters_ = len(labels_unique)
print n_clusters_

# Plot result
import matplotlib.pyplot as plt

colors = [plt.cm.Spectral(each)
          for each in np.linspace(0, 1, len(labels_unique))]
for k, col in zip(labels_unique, colors):
    #if k == -1:
        # Black used for noise.
    #    col = [0, 0, 0, 1]

    class_member_mask = (labels == k)

    xy = sensor2[class_member_mask & core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=14)

    xy = sensor2[class_member_mask & ~core_samples_mask]
    plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
             markeredgecolor='k', markersize=6)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


'''

bandwidth = estimate_bandwidth(sensor1, quantile=0.9, n_samples=560)
ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms = MeanShift()
ms.fit(sensor1)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print n_clusters_

# Plot result
import matplotlib.pyplot as plt
from itertools import cycle

plt.figure(1)
plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(sensor1[my_members, 0], sensor1[my_members, 1], sensor1[my_members, 2], sensor1[my_members, 3], sensor1[my_members, 4], sensor1[my_members, 5], col + '.')
    print sensor1[my_members].shape
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()


ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
ms = MeanShift()
ms.fit(sensor2)
labels = ms.labels_
cluster_centers = ms.cluster_centers_
labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print n_clusters_

# Plot result
import matplotlib.pyplot as plt
from itertools import cycle

plt.figure(2)
#plt.clf()

colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(sensor2[my_members, 0], sensor2[my_members, 1], sensor2[my_members, 2], sensor2[my_members, 3], sensor2[my_members, 4], sensor2[my_members, 5], col + '.')
    print sensor2[my_members].shape
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
plt.title('Estimated number of clusters_: %d' % n_clusters_)
plt.show()
'''