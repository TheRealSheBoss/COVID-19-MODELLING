#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  3 15:43:04 2022

@author: danieljoinson
"""

def clustering(file_location):
    
    import matplotlib.pyplot as plt
    import pandas as pd
    from sklearn.cluster import KMeans
    import numpy as np
    
    master_data = pd.read_csv(f'{file_location}/Master Data.csv')

    master_data_copy = master_data.copy()

    X = master_data_copy.drop(columns=['Local Authority Name', 'Region name'])
    
    def kmeans():
        
        """
        inertias = []
        K = 10
        # Loop over values of k from 1 to 10
        for k in range(1, K+1):
            # Instantiate the KMeans class with k clusters
            kmm = KMeans(n_clusters=k)
            # Fit the model to the data
            kmm.fit(X) 
            # Store the value of the inertia for this value of k
            inertias.append(kmm.inertia_)
        
        # Plot the elbow
        plt.figure()
        plt.plot(range(1, K+1), inertias, 'bx-')
        plt.xlabel('k')
        plt.ylabel('Inertia')
        plt.title('The elbow method showing the optimal k')
         
        """
        
        from sklearn.decomposition import PCA
         
        #Load Data
        
        pca = PCA(2)
         
        #Transform the data
        df = pca.fit_transform(X)
                 
        n_clus = input("How many clusters do you want to use? ")
         
        #Initialize the class object
        kmeans = KMeans(n_clusters= int(n_clus))
         
        #predict the labels of clusters.
        label = kmeans.fit_predict(df)
         
        #Getting unique labels
        u_labels = np.unique(label)
         
        #plotting the results:
        for i in u_labels:
            plt.scatter(df[label == i , 0] , df[label == i , 1] , label = i)
        plt.legend()
        plt.show()
        
        
    clustering_type = input("Do you want to use a kmeans model (K)? ")
    if clustering_type == "K":
        kmeans()
            