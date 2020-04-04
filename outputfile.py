# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo

import constants
from kmeans import *
from Aliens import *
from inputfile import *
##import pylab

class outputFile(object):
    """
    """
    def __init__(self, filename, clusterFinal, samples):
        """
        Writes the file with the closest Sample to the centroid of the cluster
        """
        self._clusters = clusterFinal
        self._filename = filename
        self._samples = samples
        self._closestExemplar = []

    def getFilename (self):
        """
        Gets the name of the input File
        """
        return self._filename

    def getClusterFinal (self):
        """
        Gets the list of Cluster
        """
        return self._clusters
    
    def setclosestExemplar (self):
        """
        Sets a list with the closest Exemplar of each Cluster
        """
        for exemplar in self.getClusterFinal():
            exemplar.setExemplar()
            self._closestExemplar.append(exemplar.getExemplar())

    def getclosestExemplar (self):
        """
        Gets the list of the closest Centroids of each cluster
        """
        return self._closestExemplar
 

    def write_file(self):
        """
        Writes the file
        """
        out_filename = self.getFilename()[:-4] + "_clusters.txt" 
        out_file = open(out_filename, 'w')            
        for i in range(len(self.getClusterFinal())):
            for k in (inputFile.getSamplesList(self._samples)):
                if self.getclosestExemplar()[i].getId() in k:
                    exemp_rep = k
            out_file.write(("#exemplar " + str(i + 1) + ':' + '\n' + str(exemp_rep) + '\n' \
            + "#cluster " + str(i + 1) + ':' + '\n').replace('[','').replace(']','').replace(",", ';').replace("'", ''))
            clusters_final = self.getClusterFinal()
            for sample in clusters_final[i].getExamples():
##                print(clusters_final[i].getExamples())
                for k in (inputFile.getSamplesList(self._samples)):
                    if sample.getId() in k:
                        cluster_rep = k
                out_file.write((str(cluster_rep) + '\n').replace('[','').replace(']','').replace(",", ';').replace("'", ''))
        out_file.close()
        
##    def graphPlotting (self):
##        """
##          Creates the graph            
##        """
##        out_filename = self.getFilename()[:-4] + "_plot.png"
##        clusters = self.getClusterFinal()
##        x = list(range(constants.FEATURE_TOTAL_LINES))
##        colours = [ "r", "g", "b", "y", 'i', 'o']
##        for i in range(len(clusters)):
##            for sample in clusters[i].getExamples():
##                pylab.plot( x, sample.getFeatures(), colours[i])
##        pylab.xticks ( x, ['heads','eyes', 'mouths', 'legs', 'tails','horns','rings','thorns','scales'])
##        pylab.xlabel('Features')
##        pylab.ylabel('Value')
##        pylab.savefig(out_filename)


