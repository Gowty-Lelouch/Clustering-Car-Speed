import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import parallel
import hdbscan
from sklearn.cluster import AgglomerativeClustering 


df = pd.read_csv('147.csv', sep=',', header=None)
df = df.iloc[:,1:3]

arr_in = df.values

arr_man = arr_in[np.where (arr_in[:,1] > 1200)] #Considering RPM below 1000 as Noise

plt.scatter(arr_man[:,0], arr_man[:,1])
plt.show()
#print('Group counts' = len(arr_man))
#for i in range(80,120,5):
#print(i)
hdbobj = AgglomerativeClustering(linkage='complete', n_clusters = 10)
hdbobj.fit(arr_man)
print('Group Count =',hdbobj.labels_.max())
print("\n")

#print(hdbobj.labels_.max())

lab = hdbobj.labels_
lab = lab.reshape(-1,1)

fin_op = np.hstack((arr_man,lab))
zero = np.empty(lab.shape)
fin_op = np.hstack((fin_op,zero))
#print(fin_op)
unique_labels = set(hdbobj.labels_)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for j in range(hdbobj.labels_.max()) :
    a = fin_op[np.where((fin_op[:,2] == j))]  #np.where returns the indices.
    xp = a[:,0]
    yp = a[:,1]
    plt.scatter(xp,yp,c=colors[j])
    plt.axis([0,120, 500, 3500])
    #plt.text(150,3400,'Alpha {}'.format(i))
   # plt.show()
    #print("Enter label \t")
    #ask = input()   #Ask contains label value
    #fin_op[[np.where((fin_op[:,2]==j))],3] = ask

#print('\n\n cluster size = ', i)

plt.show()
