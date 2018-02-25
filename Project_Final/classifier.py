import numpy as np
import matplotlib.pyplot as plt
import analysis as ans

def classify(slope, data):
    movement = []
    direction  = []
    vibration = 'blue'
    fast = 'green'
    very_fast = 'red'
    for x in slopex:
        if x >0.003 or x<-0.003:
            movement.append(very_fast)
            continue
        if -0.001 <= x <= 0.001:
            movement.append(vibration)
            continue
        if -0.003 <= x <= 0.003: 
            movement.append(fast)
            continue

    for x in ans.ax:
        if x>0:
            direction.append(1)     # Positive
        if x<0:
            direction.append(-1)    # Negative
        if x == 0:
            direction.append(0)     # No Movement

    return direction, movement


slopex = ans.slope_ax
slopey = ans.slope_ay
slopez = ans.slope_az

dir_x, mov_x = classify(slopex, ans.ax)
dir_y, mov_y = classify(slopey, ans.ay)
dir_z, mov_z = classify(slopez, ans.az)


y1 = [0.001 for x in xrange(len(slopex))] #Vibratons
y2 = [-0.001 for x in xrange(len(slopex))] #Vibratons
y3 = [0.02 for x in xrange(len(slopex))] #Fast
y4 = [-0.02 for x in xrange(len(slopex))] #Fast


'''
labels  = ['Fast', 'Very Fast', 'Vibration']
y = [j for j in xrange(len(ans.ax)-2)]
data = list(ans.ax)
data.pop()
data.pop()
plt.figure(0)
plt.plot(y, slopex, color = 'blue',label  = 'Vibration')
plt.plot(y, slopex, color = 'green',label  = 'Fast')
plt.plot(y, slopex, color = 'red',label  = 'Very Fast')
plt.scatter(y, slopex, color = mov_x)
plt.legend()
plt.figure(1)
plt.plot(y, data, color = 'blue',label  = 'Vibration')
plt.plot(y, data, color = 'green',label  = 'Fast')
plt.plot(y, data, color = 'red',label  = 'Very Fast')
plt.scatter(y, data, color = mov_z)
plt.legend()
data = list(ans.ay)
data.pop()
data.pop()
plt.figure(2)
plt.plot(y, data, color = 'blue',label  = 'Vibration')
plt.plot(y, data, color = 'green',label  = 'Fast')
plt.plot(y, data, color = 'red',label  = 'Very Fast')
plt.scatter(y, data, color = mov_y)
plt.legend()
data = list(ans.az)
data.pop()
data.pop()
plt.figure(3)
plt.plot(y, data, color = 'blue',label  = 'Vibration')
plt.plot(y, data, color = 'green',label  = 'Fast')
plt.plot(y, data, color = 'red',label  = 'Very Fast')
plt.scatter(y, data, color = mov_z)
plt.legend()
#for i in xrange(len(mov_x)):
#    plt.plot(y[i], ans.ax[i], color = str(mov_x[i]*0.5))
#plt.plot(slopey)
#plt.plot(slopez)
plt.show()
'''