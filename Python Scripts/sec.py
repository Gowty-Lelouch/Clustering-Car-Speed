import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from joblib import parallel
import hdbscan


df = pd.read_csv('147.csv', sep=',', header=None)
df = df.iloc[:,1:3]

arr_in = df.values

#arr_man = arr_in[np.where (arr_in[:,1] > 1200)] #Considering RPM below 1000 as Noise
arr_man = arr_in


#plt.scatter(arr_man[:,0], arr_man[:,1])
#plt.axis([0,120,0,3500])
#plt.show()
#print('Group counts' = len(arr_man))
#for i in range(80,120,5):
#print(i)

#-------------- HDBSCAN -------------------#

hdbobj = hdbscan.HDBSCAN(min_cluster_size =80, min_samples = 3, cluster_selection_method = 'leaf')
hdbobj.fit(arr_man)
print('Group Count =',hdbobj.labels_.max())
print("\n")

#print(hdbobj.labels_.max())

lab = hdbobj.labels_
lab = lab.reshape(-1,1)

fin_op = np.hstack((arr_man,lab))
zero = np.empty(lab.shape)
#fin_op = np.hstack((fin_op,zero))
#print(fin_op)
unique_labels = set(hdbobj.labels_)
colors = [plt.cm.Spectral(each) for each in np.linspace(0, 1, len(unique_labels))]

for j in range(hdbobj.labels_.max()) :
    a = fin_op[np.where((fin_op[:,2] == j))]  #np.where returns the indices.
    xp = a[:,0]
    yp = a[:,1]
    plt.scatter(xp,yp,c=colors[j])
    plt.axis([0,120, 0, 3500])
   #plt.text(150,3400,'Alpha {}'.format(i))
    plt.show()
    print("Enter label \t")
    ask = input()   #Ask contains label value
    zero[np.where(fin_op[:,2]==j)] = ask
#    fin_op[[np.where((fin_op[:,2]==j))],3] = ask
#    print(fin_op[:,[np.where(fin_op[:,3] == ask)]])
#print('\n\n cluster size = ', i)

#plt.show()


fin_op = np.hstack((fin_op,zero))
np.savetxt('labeled.csv', fin_op, delimiter = ',')
