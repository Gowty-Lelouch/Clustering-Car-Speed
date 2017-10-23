%Run this file in Octave / Matlab terminal.

%-------- This File is the Main script and calls other necessary functions ------------%

%Intialization
clear;
close all;
clc;

%Load csv file data into an array


arr_in = csvread('147.csv');	%Path is relative. Make sure all files are in same folder.

X = arr_in(:,2:3);	%Taking only speed, RPM and Engine load into consideration



%---- Randomly initialize centroids -----%

K = 7;	% 6 Centroids, one for each Gear + one for erroneous results at bottom

centroids = InitCentroids(X,K);	%Tested... Working..

%centroids = csvread('Centroidvals.csv');	%Using the best of Centroids from earlier runs

%--- Find Closest Centroid for each Example -----%

idx = findClosestCentroids(X,centroids);

fprintf('Closest centroids for the first 3 examples: \n')
fprintf(' %d ', idx(1:3));
fprintf('\n');


%============== Compute Means================%

centroids = computeCentroids(X, idx, K);

csvwrite('Centroidvals.csv',centroids);	%Write the centroid values to a csv file

fprintf('\nProgram Paused. Press Enter to Continue\n');
pause;


%============== K - Means clustering ==============%


max_iters = 25;

for i = 1 : max_iters

	idx = findClosestCentroids(X, centroids);
	centroids = computeCentroids(X, idx, K);

end

fprintf('Centroids computed after initial finding of closest centroids: \n')
fprintf(' %f %f \n' , centroids');

%============== Visualization ==============%

plotDataPoints(X, idx, K);
