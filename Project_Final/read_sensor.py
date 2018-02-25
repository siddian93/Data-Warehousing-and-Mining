import pandas as pd



'''
sensor1 format                      sensor2 format:
'Wearable-1'                        'Wearable-2'
'Ax'                                'Ax'
'Ay'                                'Ay'
'Az'                                'Az'
'Gx'                                'Gx'
'Gy'                                'Gy'
'Gz'                                'Gz'
'Sensor time'                       'Sensor time'
'''

class read_sensor(object):
    def __init__(self):
        print 'Accessing Sensor for Data...........'
        self.get_data()
    
    def get_data(self):
        self.sensor1 = pd.read_csv('sensor1.csv')
        self.sensor2 = pd.read_csv('sensor2.csv')
        self.sensor1.dropna(how = 'any', inplace=True)
        self.sensor2.dropna(how = 'any', inplace=True)
