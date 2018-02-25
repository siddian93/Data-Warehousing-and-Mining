import numpy as np
import pandas
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.arima_model import ARIMAResults
import matplotlib.pyplot as plt
import analysis as ans

# monkey patch around bug in ARIMA class
def __getnewargs__(self):
	return ((self.endog),(self.k_lags, self.k_diff, self.k_ma))

#ARIMA.__getnewargs__ = __getnewargs__

def train_classifier(data):
    X = data
    values = []
    reading = []
    for p in xrange(6):
        for d in xrange(2):
            for q in xrange(4):
                try:    
                    model = ARIMA(X, order=(p,d,q))
                    model_fit = model.fit()
                    #model_fit.save('model.pkl')
                    forecast = model_fit.forecast(steps = 2000)[0]
                    forecast1 = model_fit.predict(start=7, end=2000)
                    data = X
                    forecast = model_fit.forecast(steps = 100)[0]
                    forecast1 = model_fit.predict(start=len(X), end=len(X)+100)
                    reading.append(np.concatenate((data, forecast), axis=0))
                    #print len(data), "###############################################"
                    #plt.figure(i+1)
                    #plt.plot(data, label  = 'After Forecast')
                    #plt.legend()
                    values.append((p, d, q))
                except:
                    pass
    reading = np.asarray(reading)
    return reading


data_ax = train_classifier(ans.ax)
data_ay = train_classifier(ans.ay)
data_az = train_classifier(ans.az)
data_gx = train_classifier(ans.gx)
data_gy = train_classifier(ans.gy)
data_gz = train_classifier(ans.gz)
print len(data_ax)
plt.figure(0)
plt.plot(data_ax)
plt.plot(0, label = 'Predicted Ax')
plt.legend()
plt.figure(1)
plt.plot(data_ay)
plt.plot(0, label = 'Predicted Ay')
plt.legend()
plt.figure(2)
plt.plot(data_az)
plt.plot(0, label = 'Predicted Az')
plt.legend()
plt.figure(3)
plt.plot(data_gx)
plt.plot(0, label = 'Predicted Gx')
plt.legend()
plt.figure(4)
plt.plot(data_gy)
plt.plot(0, label = 'Predicted Gy')
plt.legend()
plt.figure(5)
plt.plot(data_gz)
plt.plot(0, label = 'Predicted Gz')
plt.legend()



for data in  data_ax:
    plt.figure(0)
    plt.plot(data)
plt.plot(0, label = 'Predicted Ax')
plt.legend()
for data in  data_ay:
    plt.figure(1)
    plt.plot(data)
plt.plot(0, label = 'Predicted Ay')
plt.legend()
for data in  data_az:
    plt.figure(2)
    plt.plot(data)
plt.plot(0, label = 'Predicted Az')
plt.legend()
for data in  data_gx:
    plt.figure(3)
    plt.plot(data)
plt.plot(0, label = 'Predicted Gx')
plt.legend()
for data in  data_gy:
    plt.figure(4)
    plt.plot(data)
plt.plot(0, label = 'Predicted Gy')
plt.legend()
for data in  data_gz:
    plt.figure(5)
    plt.plot(data)
plt.plot(0, label = 'Predicted Gz')
plt.legend()
plt.show()


