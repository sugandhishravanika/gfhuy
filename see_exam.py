# -*- coding: utf-8 -*-
"""see exam

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xXeGklioYLfWeDEne2DNN8xK0SdReDqk
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data=pd.read_csv("/content/Mall_Customers.csv")
print (data.head())
data.shape
data.info()
data.describe()
data.head()

x=data.iloc[:,[3,4]].values

WCSS_list = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(x)
    WCSS_list.append(kmeans.inertia_)

plt.plot(range(1, 11), WCSS_list)
plt.title('The Elbow Method Graph')
plt.xlabel('Number of clusters(k)')
plt.ylabel('WCSS_lst')
plt.show()

optimal_cluster=4
kmeans=KMeans(n_clusters=4,init='k-means++',random_state=42)
y_predict=kmeans.fit_predict(x)

plt.scatter(x[y_predict==0,0],x[y_predict==0,1],s=100,c='red',label='cluster1')
plt.scatter(x[y_predict==1,0],x[y_predict==1,1],s=100,c='blue',label='cluster2')
plt.scatter(x[y_predict==2,0],x[y_predict==2,1],s=100,c='green',label='cluster3')
plt.scatter(x[y_predict==3,0],x[y_predict==3,1],s=100,c='cyan',label='cluster4')
plt.scatter(x[y_predict==4,0],x[y_predict==4,1],s=100,c='magenta',label='cluster5') #
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='yellow',label='centroids')
plt.title('Clusters of customers')
plt.xlabel('Amount Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()