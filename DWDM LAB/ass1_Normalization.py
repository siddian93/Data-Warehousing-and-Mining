#!usr/bin/env python

import math
import numpy as np
from sklearn.datasets import load_iris

def norm_dec_scale(data, column):
    val = data[:, column].max()
    m = math.pow(10, math.ceil(math.log10(val)))
    data[:, column] /= m
    return data

def norm_min_max(data, column):
    new_min, new_max = 0, 1
    d_min = data[:, column].min()
    d_max = data[:, column].max()
    data[:, column] = ((data[:, column] - d_min)/(d_max-d_min))*(new_max - new_min) + new_min
    return data

def norm_Z_scale(data, column):
    X = sum(data[:, 3])/len(data)
    ar = np.array(data[:, column])
    sd = ar.std()
    data[:, column]  = ((data[:, column]) - X)/sd
    return data

data = load_iris().data
print data[0]
data_dS = norm_dec_scale(data, len(data[0])-1)    # This normalizes the data of the last column
print data_dS[0]
data_mm = norm_min_max(data, len(data[0])-1)
print data_mm[0]
data_Z = norm_Z_scale(data, len(data[0])-1)
print data_Z[0]