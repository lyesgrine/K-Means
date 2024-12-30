import numpy as nm    
import matplotlib.pyplot as mtp    
import pandas as pd   
from sklearn.cluster import KMeans

dataset = pd.read_csv('./Mall_Customers.csv')

x = dataset.iloc[:, [3, 4]].values  
  
wcss= []  
  
for i in range(1, 11):  
    kmeans = KMeans(n_clusters=i, init='k-means++',
                    random_state= 42)  
    kmeans.fit(x)  
    wcss.append(kmeans.inertia_)  
mtp.plot(range(1, 11), wcss)  
mtp.title('Get the Best Values for K')  
mtp.xlabel('k')  
mtp.ylabel('wcss')  
mtp.show()  

