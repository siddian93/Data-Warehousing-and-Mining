import numpy as np
from sklearn.cluster import KMeans

def generate_points():
    N  = 50
    points = [(x,y) for x in range(N) for y in range(N)]
    points = np.asarray(points)
    for i in xrange(len(points)):
        if (i%4 == 0):
            a = np.random.randint(10, 100)
            b = np.random.randint(10, 100)*2
        if (i%4 == 1):
            a = np.random.randint(150, 200)*2
            b = np.random.randint(150, 200)
        if (i%4 == 2):
            a = np.random.randint(500, 1000)
            b = np.random.randint(1, 1000)
        if (i%4 == 3):
            a = np.random.randint(200, 300)
            b = np.random.randint(200, 300)*3

        points[i, 0] = a
        points[i, 1] = b
    #print points
    #import matplotlib.pyplot as plt
    #plt.scatter(points[:, 0], points[:, 1])
    #plt.show()
    return points
    

if __name__ =='__main__':
    points = generate_points()
    random_state = 80
    y_pred = KMeans(n_clusters=4, random_state=random_state).fit_predict(points)
    print y_pred[0:16]
    import matplotlib.pyplot as plt
    #plt.subplot(211)
    #plt.scatter(points[:, 0], points[:, 1])
    plt.scatter(points[:, 0], points[:, 1], c=y_pred)
    plt.title("K-Means CLustering random number "+str(random_state))
    plt.show()
