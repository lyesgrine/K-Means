import numpy as nm    
import matplotlib.pyplot as mtp    
import pandas as pd   
from sklearn.cluster import KMeans

dataset = pd.read_csv('./Mall_Customers.csv')

x = dataset.iloc[:, [3, 4]].values  

"""
mtp.scatter(x[:,0],x[:,1], c = 'black')  
mtp.title('Row data set')  
mtp.xlabel('Annual Income (K$)')  
mtp.ylabel('Spending Score (1-100)')  
mtp.legend()  
mtp.show()   
"""
 
while (True) :
    l = int(input(">> "))
    if l == 1 :
        print(x)
    elif l == 2:
        mtp.scatter(x[:,0],x[:,1], c = 'black')  
        mtp.title('Row data set')  
        mtp.xlabel('Annual Income (K$)')  
        mtp.ylabel('Spending Score (1-100)')  
        mtp.legend()  
        mtp.show()   
    else :
        break
