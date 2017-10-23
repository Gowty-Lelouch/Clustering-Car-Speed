#import hdbscan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#import hdbscan
#import sklearn.externals.joblib.parallel.cpu_count
from joblib import parallel
import hdbscan
#import sklearn.externals.joblib

#from sklearn.cluster import DBSCAN
#from sklearn.cluster import AffinityPropagation
#from sklearn.cluster import AgglomerativeClustering

df = pd.read_csv('147.csv', sep=',',header=None)

#print(df.head(3))
print("\n\n")

df = df.iloc[:,1:3] #Make it 4 to include Engine Load

firstinput = df.values
fx = firstinput[:,0]
fy = firstinput[:,1]
plt.scatter(fx,fy)
plt.show()
#print(df.head())

#dbs = DBSCAN(eps=3, metric='euclidean', min_samples=9)
#dbs = AgglomerativeClustering(linkage='ward',n_clusters = 8)

dbs = hdbscan.HDBSCAN(min_cluster_size=100, min_samples = 60, alpha = 1.3)
dbs.fit(df)
#dbs.fit(df)
#core_samples_mask = np.zeros_like(dbs.labels_, dtype=bool)
print("\n")
labels = dbs.labels_
print(dbs.labels_.max())

#print(len(dbs.labels_))
#print(labels.shape)
lab = labels.reshape(-1,1)
dfnp = df.values    #Input as numpy array
    
#Trying for Visualization

#print((dfnp.shape))
fin = np.hstack((dfnp,lab[:,-1:]))
#print(fin)
#print(len(fin))
unique_labels = set(labels)
colors = [plt.cm.Spectral(each) for each in np.linspace(0,1,len(unique_labels))]
#col = ['r','b','g','v','y','k']
for i in range(8):
    a = fin[np.where((fin[:,2] == i))]  #np.where returns the indices.
    print('\n\n')
    xp = a[:,0]
    yp = a[:,1]
    plt.scatter(xp,yp,c=colors[i])
    plt.show()
