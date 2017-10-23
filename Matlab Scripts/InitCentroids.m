function centroids = InitCentroids(X, K)
%KMEANSINITCENTROIDS This function initializes K centroids that are to be 
%used in K-Means on the dataset X
%   centroids = KMEANSINITCENTROIDS(X, K) returns K initial centroids to be
%   used with the K-Means on the dataset X
%

% You should return this values correctly
centroids = zeros(K, size(X, 2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should set centroids to randomly chosen examples from
%               the dataset X
%


%Randomly reorder the indices
%Randperm returns the indices in random order

randindex = randperm(size(X,1));

%Select first 6 indices

centroids = X(randindex(1:K),:);





% =============================================================

end

