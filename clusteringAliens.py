# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo

from Aliens import *
from inputfile import *
from kmeans import *
from outputfile import *
import constants
import sys

number_clusters = int (sys.argv[1])
number_trials = int (sys.argv[2])
file_name = str(sys.argv[3])

def main():
    input_f = inputFile(file_name)
    input_f.setExemplars()
    input_f.setSamples()
    if "void" in input_f.getExemplarsList():
        centroids = input_f.getExemplarsList()
    else:
        centroids= input_f.getAlienExemplars()
        if "void" not in input_f.getExemplarsList():
            assert len(input_f.getAlienExemplars()) == number_clusters, 'Invalid Input: Number of Clusters [k] does not match the Number of Provided Inicial Centroids'
            assert number_trials == 1, ' Invalid Input. When Initial Centroids are provided the Number of Trials [t] should be 1.'        
    samples = input_f.getAlienSamples()
    assign = kmeansclustering()
    assign.trykmeans(samples, Alien, number_clusters, number_trials, centroids, False)
    
    output_f = outputFile(file_name, assign.getKmeans(), input_f)
    output_f.setclosestExemplar()
    output_f.write_file()
##    output_f.graphPlotting()
    


main()
