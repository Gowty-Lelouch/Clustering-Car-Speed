%%%---------- Readme File ----------%%%

File "Prop Rpms.csv" is the final output file with Gear labels attached.

Contents
	Matlab Scripts
	Python Scripts

To Run :

	Run the File "sec.py" from the directory Python Scripts

		Dependencies Required :
			1. Python 3.5
			2. Scikit Learn
			3. Numpy
			4. Pandas
			5. Matplotlib
			6. Cython
			7. HDBSCAN
			8. joblib (Import as from joblib import parallel)
	The file reads the input csv file, and runs HDBSCAN, a variant of DBSCAN Clustering.

	To read the Gear calculation details, please refer to "Gear Ratio Calculation.txt"

How I did..?

	1. First I tried, the most common clustering algorithm, "K - Means", but due to its tendency to select globular clusters, it failed.

	2. Then I read the differences about various clustering algorithms, and shortlisted DBSCAN, Hierarchial, OPTICS, and CURE

	3. Due to implementational difficulties, I reduced the list to DBSCAN and Hierarchial

	4. Implemented DBSCAN in Matlab, only to encounter "Out of Memory" error. My laptop's specifications weren't enough. Well, I'm running on 2GB RAM system :D :D

	5. Then came to Python.

	6. Implemented Hierarchial with linkage type as "Complete". It took huge time, yet the results were almost identical to "K - Means". Again a setback.

	7. Tried DBSCAN next with different parameters, but couldn't find any good solutions.

	8. After some googling, found out that a better version of DBSCAN existed, called HDBSCAN.

	9. Implemented that using the HDBSCAN module.

	10. After fiddling with the paramters a lot, I had to compromise.

Finally chose, the paramters such that there won't be too many clusters and also covers most points.

Plotted, the graph, and manually compared it with input, and gave the appropriate gear for each cluster Groups.

After that, used the Excel formulas, to compute the Gear Ratio.

For answers regarding the questions, please read, answers.md file
