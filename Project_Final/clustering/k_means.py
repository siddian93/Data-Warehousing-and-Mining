import numpy as np 
import scipy as sp
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

data  = load_iris().data
labels = load_iris().target

train_data, test_data, train_label, test_label = train_test_split(data, labels, test_size = 0.3, random_state = 42)

kmeans = KMeans(n_clusters=3, random_state=None)
clusters  = kmeans.fit(train_data)
pred_labels = kmeans.predict(test_data)
x = np.zeros(len(train_data))
y = np.zeros(len(train_data))

x1 = np.zeros(len(test_data))
y1 = np.zeros(len(test_data))

for i in xrange(len(train_data)):
    x[i] = np.sqrt(np.power(train_data[i][0], 2)+np.power(train_data[i][1], 2))
    y[i] = np.sqrt(np.power(train_data[i][2], 2)+np.power(train_data[i][3], 2))

for i in xrange(len(test_data)):
    x1[i] = np.sqrt(np.power(test_data[i][0], 2)+np.power(test_data[i][1], 2))
    y1[i] = np.sqrt(np.power(test_data[i][2], 2)+np.power(test_data[i][3], 2))

print pred_labels
print test_label

plt.scatter(x, y, c = kmeans.labels_, s = 100)
plt.scatter(x1, y1, c = pred_labels, s = 50)


#plt.scatter(data[clusters == 0, 0], data[clusters == 0, 1])
plt.show()
