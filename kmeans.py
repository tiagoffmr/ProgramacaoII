# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo
##import pylab

import math
import random
import constants
from Cluster import *
from Aliens import *
from inputfile import *

   


class kmeansclustering ():
    

    def kmeans(self, examples, exampleType, k,  iCentroids, verbose):
        """
        K-means clustering
        
        Requires:
        examples a list of examples of type exampleType;
        exampleType represents the type of the examples;
        k positive int, number of clusters;
        verbose Boolean, printing details on/off
        Ensures:
        list containing k clusters;
        if verbose is True, result of each iteration
        of k-means is printed
        """
        
        if "void" in iCentroids:     
        #Get k randomly chosen initial centroids, create cluster for each
            initialCentroids = random.sample(examples, k)
        else:
            initialCentroids = iCentroids
    ##        print('3')

        clusters = []
        for e in initialCentroids:
            clusters.append(Cluster([e], exampleType))
        #Iterate until centroids do not change
        converged = False
        numIterations = 0
        while not converged:
            numIterations += 1
            #Create a list containing k distinct empty lists
            newClusters = []
            for i in range(k):
                newClusters.append([])

            #Associate each example with closest centroid
            for e in examples:
                #Find the centroid closest to e
                smallestDistance = e.distance(clusters[0].getCentroid())
                index = 0
                for i in range(1, k):
                    distance = e.distance(clusters[i].getCentroid())
                    if distance < smallestDistance:
                        smallestDistance = distance
                        index = i
                #Add e to the list of examples for the appropriate cluster
                newClusters[index].append(e)

            #Avoid having empty clusters
            for c in newClusters:
                if len(c) == 0:
                    raise ValueError("Empty Cluster")
            #Update each cluster; check if a centroid has changed
            converged = True
            for i in range(len(clusters)):
                if clusters[i].update(newClusters[i]) > 0.0:
                    converged = False
            if verbose:
                print('Iteration #' + str(numIterations))
                for c in clusters:
                    print(c)
                print('') #add blank line
        return clusters



    def dissimilarity(self, clusters):
        """
        Dissimilarity among clusters

        Ensures:
        dissimilarity among clusters as the summation
        of each cluster variance
        """
        totDist = 0.0
        for c in clusters:
            totDist += c.variance()
        return totDist



    def trykmeans(self, examples, exampleType, numClusters, numTrials, iCentroids,
                  verbose = False):
        """
        Best clustering outcome within a given number of trials
        of k-means clustering

        Requires:
        examples a list of examples of type exampleType;
        exampleType represents the type of the examples;
        numClusters positive int, number of clusters;
        numTrials positive int, number of trials with k-means clustering
        Ensures:
        The clusters obtained with the lowest dissimilarity among them
        after running k-means clustering numTrials times over examples
        """
        self._best = self.kmeans(examples, exampleType, numClusters, iCentroids, verbose)
        minDissimilarity = self.dissimilarity(self._best)
        
        for trial in range(1, numTrials):
            clusters = self.kmeans(examples, exampleType, numClusters, iCentroids, verbose)
            currDissimilarity = self.dissimilarity(clusters)
            if currDissimilarity < minDissimilarity:
                self._best = clusters
                minDissimilarity = currDissimilarity


    
    def getKmeans (self):
        """
        Gets the list of the best clusters calculated using trykmeans
        """
        return self._best
