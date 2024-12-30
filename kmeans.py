import numpy as nm    
import matplotlib.pyplot as mtp    
import pandas as pd   
from sklearn.cluster import KMeans

dataset = pd.read_csv('./Mall_Customers.csv')
x = dataset.iloc[:, [3, 4]].values  

colors = ['yellow','red','pink','blue','green',
          'magenta','purple','black','cyon']
n = int(input('Number Of Clusters k : '))

kmeans = KMeans(n_clusters=n, init='k-means++',
                random_state= 42)  
y_predict= kmeans.fit_predict(x) 

for i in range(0,n):
    mtp.scatter(x[y_predict == i, 0],
                x[y_predict == i, 1],
                s = 100, c = colors[i],
                label = 'Cluster '+str(i+1))  
mtp.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s = 100, c = 'navy', label = 'Centroid')

mtp.title('K-means Algorithm')  
mtp.xlabel('Annual Income (K$)')  
mtp.ylabel('Spending Score (1-100)')  
mtp.legend()  
mtp.show()  

    