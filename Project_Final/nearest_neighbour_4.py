import numpy as np
import pandas as pd
import analysis as ans
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from time import time

def find_sse(cluster, data, n_clusters):
    avg = 0.0
    sse = 0.0
    for j in xrange(3):
        deviation  = []
        for i in cluster[j]:
            avg+=data[i]
        avg = avg/len(cluster[j])
        for i in cluster[j]:
            deviation.append(np.absolute(data[i] -  avg))
        deviation = np.power(deviation, 2)
        sse+=sum(deviation)
    #print sse
    return sse

def nearest_neighbour_classifier(data):
    avg_data = sum(data)/len(data)
    cluster, cluster_final = [[], [], []], [[], [], []]
    distance = [[], [], []]
    n_clusters  = 3
    min_sse = 9999999999999.9
    time_start  = time()
    time_end = 0.0
    time_to_finish = 0.0
    for i in xrange(len(data)):
        for j in xrange(len(data)):
            for k in xrange(len(data)):
                if k == 1 and i == 0 and j == 0:
                    time_to_finish = np.ceil(((time_end - time_start)*len(data)*len(data)*len(data)/60))
                    print "Time to finish : %.2f Minutes" %time_to_finish
                cluster = [[], [], []]
                distance = [[], [], []]
                if i == j or i == k or j == k :
                    pass
                cluster[0].append(i)
                cluster[1].append(j)
                cluster[2].append(k)
                for l in xrange(len(data)):
                    distance[0].append(np.absolute(data[cluster[0][0]] - data[l]))
                    distance[1].append(np.absolute(data[cluster[1][0]] - data[l]))
                    distance[2].append(np.absolute(data[cluster[2][0]] - data[l]))
                # for l in xrange(len(data)):
                #     distance[1].append(np.absolute(data[cluster[1][0]] - data[l]))
                # for l in xrange(len(data)):
                #     distance[2].append(np.absolute(data[cluster[2][0]] - data[l]))

                for l in xrange(len(data)):
                    if distance[0][l]<distance[1][l] and distance[0][l]<distance[2][l]:
                        cluster[0].append(l)
                    elif distance[1][l]<distance[0][l] and distance[1][l]<distance[2][l]:
                        cluster[1].append(l)
                    elif distance[2][l]<distance[1][l] and distance[2][l]<distance[0][l]:
                        cluster[2].append(l)
                #print cluster
                sse = find_sse(cluster, data, 3)
                if min_sse >= sse and len(cluster[0])>len(data)/5 and len(cluster[1])>len(data)/5 and len(cluster[2])>len(data)/5:
                    min_sse = sse
                    cluster_final = cluster
                #print cluster
                time_end = time()
        
    #print len(data) == (len(cluster[0])+len(cluster[1])+len(cluster[2]))
    return cluster_final
    plt.show()


file_no  = '3'
n1 = 201
n2 = 300
print 'Classifying Ax ###########################' 
cluster_ax = nearest_neighbour_classifier(ans.ax[n1:n2])
print 'Classifying Ay ###########################'
cluster_ay = nearest_neighbour_classifier(ans.ay[n1:n2])
print 'Classifying Az ###########################'
cluster_az = nearest_neighbour_classifier(ans.az[n1:n2])
print 'Classifying Gx ###########################'
cluster_gx = nearest_neighbour_classifier(ans.gx[n1:n2])
print 'Classifying Gy ###########################'
cluster_gy = nearest_neighbour_classifier(ans.gy[n1:n2])
print 'Classifying Gz ###########################'
cluster_gz = nearest_neighbour_classifier(ans.gz[n1:n2])
print 'Classifying Slope_Ax ###########################'
cluster_slope_ax = nearest_neighbour_classifier(ans.slope_ax[n1:n2])
print 'Classifying Slope_Ay ###########################'
cluster_slope_ay = nearest_neighbour_classifier(ans.slope_ay[n1:n2])
print 'Classifying Slope_Az ###########################'
cluster_slope_az = nearest_neighbour_classifier(ans.slope_az[n1:n2])
print 'Classifying Velocity_x ###########################'
cluster_vx = nearest_neighbour_classifier(ans.vx[n1:n2])
print 'Classifying Velocity_y ###########################'
cluster_vy = nearest_neighbour_classifier(ans.vy[n1:n2])
print 'Classifying Velocity_z ###########################'
cluster_vz = nearest_neighbour_classifier(ans.vz[n1:n2])
print 'Classifying Angular Velocity_x ###########################'
cluster_ox = nearest_neighbour_classifier(ans.ox[n1:n2])
print 'Classifying Angular Velocity_y ###########################'
cluster_oy = nearest_neighbour_classifier(ans.oy[n1:n2])
print 'Classifying Angular Velocity_z ###########################'
cluster_oz = nearest_neighbour_classifier(ans.oz[n1:n2])



df = pd.DataFrame(cluster_ax)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_ax.csv', index = False)
df = pd.DataFrame(cluster_ay)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_ay.csv', index = False)
df = pd.DataFrame(cluster_az)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_az.csv', index = False)
df = pd.DataFrame(cluster_gx)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_gx.csv', index = False)
df = pd.DataFrame(cluster_gy)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_gy.csv', index = False)
df = pd.DataFrame(cluster_gz)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_gz.csv', index = False)
df = pd.DataFrame(cluster_slope_ax)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_slope_ax.csv', index = False)
df = pd.DataFrame(cluster_slope_ay)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_slope_ay.csv', index = False)
df = pd.DataFrame(cluster_slope_az)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_slope_az.csv', index = False)
df = pd.DataFrame(cluster_vx)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_vx.csv', index = False)
df = pd.DataFrame(cluster_vz)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_vz.csv', index = False)
df = pd.DataFrame(cluster_vy)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_vy.csv', index = False)
df = pd.DataFrame(cluster_oy)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_oy.csv', index = False)
df = pd.DataFrame(cluster_ox)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_ox.csv', index = False)
df = pd.DataFrame(cluster_oz)
path_to_cluster = '/home/siddhartha/dwm/project_beta/Clusters/'
df.to_csv(path_to_cluster+file_no+'cluster_oz.csv', index = False)


#print df