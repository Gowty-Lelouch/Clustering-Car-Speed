1. Possible Clustering Algorithms

	1. K Means
	2. Mean Shift
	3. Spectral
	4. Hirerachial / Agglomerative
	5. Density Based (DBSCAN, OPTICS)
	6. CURE
	7. BIRCH

2. Finding out Gear ratios.

	Details and assumptions made with Gear ratio calculation are in the file "Gear Ratio Calculation.txt". The final output is in "Prop Rpms.csv" file.
	
	Regarding the change of Gear ratio with time, I hope that calculating Wheel RPM and then Prop shaft RPM, instead of using Number of Teeth in driven gear, will help in the issue, as the speed indicated will account for the change in Gear ratio, instead of the constant number of teeth metric

3. Running Prototype.

	Out of the above mentioned clustering algorithms, I avoided "K - Means, Mean - Shift, Agglomerative, BIRCH" algorithms, due to their tendency to form globular clusters. But since, the data isn't a glob, K means and Agglomerative method failed, and returned similar results.

	I implemented a variant of DBSCAN, called HDBSCAN proposed by the same authors as DBSCAN. For Gear ratio values, please scroll to the end of this file.

	To remove Noise, fiddling with minimum number of samples paramter helped, but due to the nature of the data, it resulted in loss of labels for many data points, as they got clustered as Noise and were ignored.

	Although, removing all the data below 1000 RPM had quite good results (Not done here as it ended up in removing around 5000 data points)

	I feel like, a better data acquisition system is the way to go.

4. Location Info

	I assume, areas near equator to have higher temperature, thereby resulting in a higher IDLE RPM. But, what can I do with this ? I really don't know.

	May be I can look for the driving habit of majority of people of a particular region, or use a distance metric to compare the differences in driving at different places.
