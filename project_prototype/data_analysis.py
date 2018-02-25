import numpy as np
import pyexcel as pe 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

sheet = pe.get_sheet(file_name='KitCat.xlsx')
data = []
ip2 = '192.168.43.159'
ip1 = '192.168.43.70'
head1, head2 = [], []
sensor1, sensor2 = [], []
for record in sheet:
    data.append(record)

heads = data.pop(0)

for i in xrange(len(heads)) : 
    if heads[i] == '':
        break
    head1.append(heads[i])

head2 = head1


for i in xrange(len(data)):
    while '' in data[i]:
        data[i].remove('')
    if data[i][0] == ip1:
        sensor1.append(data[i])
    else :
        sensor2.append(data[i])

sensor1, sensor2 = np.asarray(sensor1), np.asarray(sensor2)
#plt.plot(sensor1[:, len(sensor1[0])-1], sensor1[:, 1])
#plt.plot(sensor1[:, len(sensor1[0])-1], sensor1[:, 2])
temp = []
count = 0
for x in sensor1:
    #print float(x[1])
    temp.append([float(x[1]), count])
    count+=1

temp = np.asarray(temp)
y_pred = KMeans(n_clusters=3, random_state=50).fit_predict(temp)
#plt.plot(temp[:, 0], c=y_pred)
l1, l2, l3 = [], [], []
for i in xrange(len(temp)):
    x = y_pred[i]
    y = temp[i]
    if x == 0:
        l1.append(y[0])
    if x == 1:
        l2.append(y[0])
    if x==2:
        l3.append(y[0])
plt.plot(l1)
plt.plot(l2)
plt.plot(l3)

#print head1
f, axarr = plt.subplots(3, sharex=True)
f1,sub_plt = plt.subplots(3, sharex=True)
axarr[0].plot(sensor1[:, 1])
axarr[0].set_title('Ax')
axarr[1].plot(sensor1[:, 2])
axarr[1].set_title('Ay')
axarr[2].plot(sensor1[:, 3])
axarr[2].set_title('Az')
sub_plt[0].plot(sensor1[:, 4])
sub_plt[0].set_title('Gx')
sub_plt[1].plot(sensor1[:, 5])
sub_plt[1].set_title('Gy')
sub_plt[2].plot(sensor1[:, 6])
sub_plt[2].set_title('Gz')
plt.show()


#for i in xrange(1,len(head1)-1):
#    plt.plot(sensor1[: 50, i])
#plt.show()
