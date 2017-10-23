%-------- This File is the Main script and calls other necessary functions ------------%

%Intialization
clear;
close all;
clc;


%======= Import Data =======%

arr_in = csvread('147.csv');	%Path is relative. Make sure all files are in same folder.

X = arr_in(:,2:3);	%Taking only speed, RPM and Engine load into consideration


%===== Trial =====%

[clus_label, varType] = dbscan(X,20)
