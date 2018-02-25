import numpy as np
import pyexcel as pe 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class Sensors_Data(object):
    def __init__(self):
        print 'Sensors Innitialized'
        self.get_data()


    def get_data(self):
        sheet = pe.get_sheet(file_name='KitCat.xlsx')
        data = []
        self.ip2 = '192.168.43.159'
        self.ip1 = '192.168.43.70'
        self.header= []
        self.sensor1, self.sensor2 = [], []
        
        for record in sheet:
            data.append(record)

        heads = data.pop(0)

        for i in xrange(len(heads)) : 
            if heads[i] == '':
                break
            self.header.append(heads[i])


        for i in xrange(len(data)):
            while '' in data[i]:
                data[i].remove('')
            if data[i][0] == self.ip1:
                self.sensor1.append(data[i])
            else :
                self.sensor2.append(data[i])

        self.sensor1, self.sensor2 = np.asarray(self.sensor1), np.asarray(self.sensor2)

        self.data_s1, self.data_s2 = np.zeros((len(self.sensor1), 6)), np.zeros((len(self.sensor2), 6))

        for i in xrange(len(self.sensor1)):
            for j in xrange(1, 7):
                self.data_s1[i][j-1] = np.float64(self.sensor1[i][j])
        
        for i in xrange(len(self.sensor2)):
            for j in xrange(1, 7):
                self.data_s2[i][j-1] = np.float64(self.sensor2[i][j])
        
        self.data_s1, self.data_s2 = np.asarray(self.data_s1), np.asarray(self.data_s2)
        #return self.header, sensor1, sensor2
