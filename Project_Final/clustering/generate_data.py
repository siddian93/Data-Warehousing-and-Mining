import numpy as np

dim = input('Enter Number of Dimensions : ')
train_data = np.random.rand(15000, dim)
test_data = np.random.rand(150, dim)

from sklearn.cluster import KMeans
from generate_data import train_data, test_data

kmeans  = KMeans(n_clusters=10, random_state=None)
clusters = kmeans.fit(train_data)
train_labels = kmeans.labels_
pred_labels = kmeans.predict(test_data)

np.savetxt('labels_testing.csv', pred_labels.astype(np.float64), fmt='%f', delimiter=',')
np.savetxt('labels_training.csv', kmeans.labels_.astype(np.float64), fmt='%f', delimiter=',')
np.savetxt('dataset_training.csv', train_data.astype(np.float64), fmt='%f', delimiter=',')
np.savetxt('dataset_testing.csv', test_data.astype(np.float64), fmt='%f', delimiter=',')