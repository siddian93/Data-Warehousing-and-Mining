import numpy as np
import scipy as sp
import smoothing as smooth
from read_sensor import read_sensor
from matplotlib import pyplot as plt


def map_linear_acceleration(accelx, accely, accelz):
    vx, vy, vz = [], [], []
    for x in accelx:
        if x<0:
            vx.append(-np.exp(pow(-x, 10)/9.8))
        else :    
            vx.append(np.exp(pow(x, 10)/9.8))
    for x in accely:
        if x<0:
            vy.append(-np.exp(pow(-x, 10)/9.8))
        else :    
            vy.append(np.exp(pow(x, 10)/9.8))
    for x in accelz:
        if x<0:
            vz.append(-np.exp(pow(-x, 10)/9.8))
        else :    
            vz.append(np.exp(pow(x, 10)/9.8))
    vx = np.asarray(vx)
    vy = np.asarray(vy)
    vz = np.asarray(vz)
    return vx, vy, vz


def map_angular_acceleration(accelx, accely, accelz):
    ox, oy, oz = [], [], []
    for x in accelx:
        ox.append(x*np.tan(3*np.pi*x/5))
        
    for x in accely:
        oy.append(x*np.tan(3*np.pi*x/5))
        
    for x in accelz:
        oz.append(x*np.tan(3*np.pi*x/5))
    ox = smooth.savitzky_golay(ox, 101, 3)
    oy = smooth.savitzky_golay(oy, 101, 3)
    oz = smooth.savitzky_golay(oz, 101, 3)
    return ox, oy, oz    

def linear_acceleration(ax, ay, az):
    slope_ax, slope_ay, slope_az = [], [], []

    for i in xrange(1, len(ax)-1):
        slope_ay.append(ay[i+1] - ay[i])

    for i in xrange(1, len(ax)-1):
        slope_az.append(az[i+1] - az[i])

    for i in xrange(1, len(ax)-1):
        slope_ax.append(ax[i+1] - ax[i])

    slope_ax = np.asarray(slope_ax, dtype='float64')
    slope_ay = np.asarray(slope_ay, dtype='float64')
    slope_az = np.asarray(slope_az, dtype='float64')

    slope_ax = smooth.savitzky_golay(slope_ax, 101, 3)
    slope_ay = smooth.savitzky_golay(slope_ay, 101, 3)
    slope_az = smooth.savitzky_golay(slope_az, 101, 3)
    return slope_ax, slope_ay, slope_az

def angular_accelration(gx, gy, gz):
    slope_gx, slope_gy, slope_gz = [], [], []

    for i in xrange(1, len(gy)-1):
        slope_gy.append(gy[i+1] - gy[i])

    for i in xrange(1, len(gz)-1):
        slope_gz.append(gz[i+1] - gz[i])

    for i in xrange(1, len(gx)-1):
        slope_gx.append(gx[i+1] - gx[i])

    slope_gx = np.asarray(slope_gx, dtype='float64')
    slope_gy = np.asarray(slope_gy, dtype='float64')
    slope_gz = np.asarray(slope_gz, dtype='float64')

    slope_gx = smooth.savitzky_golay(slope_gx, 101, 3)
    slope_gy = smooth.savitzky_golay(slope_gy, 101, 3)
    slope_gz = smooth.savitzky_golay(slope_gz, 101, 3)
    return slope_gx, slope_gy, slope_gz

def linear_velocity(ax, ay, az):
    vx, vy, vz = [], [], []
    vx, vy, vz = map_linear_acceleration(ax, ay, az)
    return vx, vy, vz

def angular_veloctiy(gx, gy, gz):
    ox, oy, oz = [], [], []
    ox, oy, oz = map_angular_acceleration(gx, gy, gz)
    return  ox, oy, oz


read = read_sensor()
sensor1 = read.sensor1
sensor2 = read.sensor2

ax = np.asarray(sensor1['Ax'], dtype = 'float64')
ay = np.asarray(sensor1['Ay'], dtype = 'float64')
az = np.asarray(sensor1['Az'], dtype = 'float64')

gx = np.asarray(sensor1['Gx'], dtype = 'float64')
gy = np.asarray(sensor1['Gy'], dtype = 'float64')
gz = np.asarray(sensor1['Gz'], dtype = 'float64')

#Smoothing
raw_ax = ax
ax = smooth.savitzky_golay(ax, 101, 3)
ay = smooth.savitzky_golay(ay, 101, 3)
az = smooth.savitzky_golay(az, 101, 3)

raw_gx = gz
gx = smooth.savitzky_golay(gx, 101, 3)
gy = smooth.savitzky_golay(gy, 101, 3)
gz = smooth.savitzky_golay(gz, 101, 3)

#Slope of Data
slope_ax, slope_ay, slope_az = linear_acceleration(ax, ay, az)
slope_gx, slope_gy, slope_gz = angular_accelration(gx, gy, gz)

#Velocity
vx, vy, vz = linear_velocity(ax, ay, az)
ox, oy, oz = angular_veloctiy(gx, gy, gz)
#plt.figure(3)
#plt.plot(ax[:20], label = 'Ax')
#plt.legend()
#plt.show()


plt.figure(1)
legend_ax, = plt.plot(slope_ax, label = 'Slope Ax')
legend_ay, = plt.plot(slope_ay, label = 'Slope Ay')
legend_az, = plt.plot(slope_az, label = 'Slope Az')
plt.legend()
plt.figure(2)
plt.plot(slope_gx, label = 'Slope Gx')
plt.plot(slope_gy, label = 'Slope Gy')
plt.plot(slope_gz, label = 'Slope Gz')
plt.legend()
plt.figure(3)
plt.plot(raw_ax, label = 'Raw Points')
plt.plot(ax, label = 'Ax', color = 'red')
#plt.plot(ay, label = 'Ay')
#plt.plot(az, label = 'Az')
plt.legend()
plt.figure(7)
plt.plot(raw_gx, label = 'Raw Points')
plt.plot(gz, label = 'Ax', color = 'red')
plt.figure(4)
plt.plot(gx, label = 'Gx')
plt.plot(gy, label = 'Gy')
plt.plot(gz, label = 'Gz')
plt.legend()
plt.figure(5)
plt.plot(vx, label = 'Vx')
plt.plot(vy, label = 'Vy')
plt.plot(vz, label = 'Vz')
plt.legend()
plt.figure(6)
plt.plot(ox, label = 'Ang_Vx')
plt.plot(oy, label = 'Ang_Vy')
plt.plot(oz, label = 'Ang_Vz')
plt.legend()
plt.show()
