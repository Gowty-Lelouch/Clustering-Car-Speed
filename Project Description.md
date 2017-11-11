#Problem Statement

Every day a lot of people drive cars, especially in countries like India, cars with _manual transmission_ are quite abundant. Not everyone, knows the knack of when to change the _Gear_ to get good **fuel Economy**. But, by changing _gears at correct RPMs_ we can increase the _fuel economy_.

The purpose of this code, is to _**Cluster**_ the _**Speed and RPM**_ data of a car and to _label_ them with _**respective gears**_ using _Unsupervised Learning_. The data is taken from ODB port of a car.

##Model Selection

The first step in the process, was to visualise the data using differnt plots. Time series plotting didn't gave any useful information even though the data is a sampled per _2 seconds_. *Scatter plot* of _Speed vs RPM_ gave an insight on how the data is organised.

Since, the data had quite conisderable amount of Noise, (deduced through looking at the plot), I had to remove it by selecting data below IDLE RPM as Noise.

As this is a labelling problem, I resorted to using Clustering alogrithms.

###Selecting the Algorithm (TL;DR : Density based Algorithm Chosen)

I had K-Means, Mean - Shift, BIRCH, Hirearchial (Agglomerative), DBSCAN, HDBSCAN and CURE algorithms in mind. First, applied K - Means, using MATLAB, but since it was a **Centroid** based algorithm, the algorithm chose **Circular blobs** and didn't provided _intended results_. The next, I tried with Agglomerative clustering algorithm, it again provided a similar result as K-Means. Also, Matlab was taking too much time, even to compute this (All thanks to my laptop's specs). 

After, that I looked for _Density based_ clustering algorithms, which won't tend to choose only **globular clusters**. DBSCAN looked like it would do the trick. But unfortunately, MATLAB threw **out of Memory** error. So, I resorted to using Python.


##Performance

The Sci-kit learn module, had the DBSCAN algorithm function, which needed a _radius_ and _minimum of number of neighbours_ parameter. After some trial and error the algorithm failed to produce acceptable results even with wide range of parameter changes. The _variable density_ of the data was a _bottleneck_ for the algo.

Hence, used HDBSCAN - a variant of DBSCAN, which works better with data of variable density, proposed by the same authors as the DBSCAN and comes with the Module **HDBSCAN** (Requires Cython)

##Problems Faced

Even with HDSCAN, and after carefully adjusting the paramters and verifying it by visualization, the results weren't that great. And, my Laptop was already taking too much time to compute the results.

Having a smaller _minimum cluster size_ and _minimum samples_ gave too many small clusters, but included every data points. Having a larger value gave small number of big clusters but neglected too many data points as noise. So, as a tradeoff between having less number of clusters and not losing data points as noise, I chose the parameters such that it gave a total of 64 clusters and neglected near to 3000 data points (out of 13000 approx) as noise.

After that, I cross verified the clusters with the original image and labelled (gave correct gear numbers) them appropriately.

##Finding out the Gear ratio

Considering the car to be _Swift Dezire_ and using the _Tire size_ and _Final drive_ details of the car, I calculated the gear ratios. But, the answers obtained varied from the original (as mentioned in the official specification sheet) by 20 percent. The calculations can be found in **Gear Ratio Calculation.txt**

##Limitations

With the present algorithm, I have to manually cross verify too many clusters, a better algorithm that works well on irregular leaf shapes will work better. Also, too many data gets discared as noise as we choose a high value for _minimum cluster size_. After learning more about _Data Cleaning_ and understanding the intricacies in choosing a model, I would like to implement the problem with CURE and OPTICS. I may even write my own algorithm after learning the details. As for now, I can implement K - Means on my own without using the library functions.

