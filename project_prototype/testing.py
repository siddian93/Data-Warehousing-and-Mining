import numpy as np
from read_sensor import Sensors_Data
#from scipy import interpolate
import smoothing as smooth
import matplotlib.pyplot as plt

sd = Sensors_Data()
s1, s2  = sd.data_s1, sd.data_s2
t1 = (sd.sensor1)
p1 = t1[:, len(t1[0])-1]
p1  = np.asarray(p1)
t1 = np.float64(t1[:, len(t1[0])-1])
s_0  = smooth.savitzky_golay(s1[:, 0], 101, 3)
s_1  = smooth.savitzky_golay(s1[:, 1], 101, 3)
s_2  = smooth.savitzky_golay(s1[:, 2], 101, 3)
s_3  = smooth.savitzky_golay(s1[:, 3], 101, 3)
s_4  = smooth.savitzky_golay(s1[:, 4], 101, 3)
s_5  = smooth.savitzky_golay(s1[:, 5], 101, 3)

val = 0
s1_dict = {}
for i in xrange(len(t1)):
    key = t1[i]
    if s1_dict.has_key(key):
        s1_dict[key] +=1
    else :
        s1_dict[key] = 1 

for i in sorted(s1_dict):
    print i, ':', s1_dict[i]

#plt.plot(s1[:, 0], 'green')
plt.plot(s_0)
plt.plot(s_1)
plt.plot(s_2)
plt.show()
plt.plot(s_3)
plt.plot(s_4)
plt.plot(s_5)


plt.show()

'''
#t1 = t1/1e8
#print t1

mean = 0
deviation = np.absolute(s1[:, 0] - 0)
diff = sum(deviation)/len(deviation)

for i in xrange(len(s1)):
    if s1[i][0] < 0:
        s1[i][0] += diff
    if s1[i][0] > 0:
        s1[i][0] -= diff

t_uniq = np.unique(t1)
l1 = sd.sensor1
#print np.asarray(l1)

s1_dict = {}
for i in xrange(len(l1)):
    key = np.float64(l1[i][7])
    val = np.float64(l1[i][1])
    s1_dict[key] = val

print len(s1_dict), len(t_uniq)

ax = []
for i in s1_dict:
    ax.append(s1_dict[i])

ax = np.asarray(ax)
print len(ax), len(t_uniq)
#f  = interpolate.interp1d(t_uniq, ax)
#new_ax = f(ax)
#plt.plot(t1, new_ax)
plt.plot(t_uniq, ax)


f, axarr = plt.subplots(7, sharex=True)
axarr[0].plot(t1, s1[:, 0])
axarr[0].set_title('Ax') 
axarr[1].plot(t1, s1[:, 1])
axarr[1].set_title('Ay')
axarr[2].plot(t1, s1[:, 2])
axarr[2].set_title('Az')
axarr[3].plot(t1, s1[:, 3])
axarr[3].set_title('Gx')
axarr[4].plot(t1, s1[:, 4])
axarr[4].set_title('Gy')
axarr[5].plot(t1, s1[:, 5])
axarr[5].set_title('Gz')
axarr[6].plot(t1, deviation)
axarr[6].set_title('Az Deviation')

plt.show()
'''
 