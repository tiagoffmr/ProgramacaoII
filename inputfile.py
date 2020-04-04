# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo

import constants
from Aliens import *



class inputFile(object):
    
    def __init__(self, filename):
        """
        Reads the file
        """
        self._mySamples=[]
        self._exemplarsList=[]
        self._samplesList=[]
        self._totalList = []
        self._alienSamples = []
        self._ExemplarsEnd = 0
        self._SamplesStart = 0
        self._ExemplarsVoid= 0
        in_file= open(filename)
        for line in in_file:
            self._mySamples.append(line)
        in_file.close()

        for j in range(len(self._mySamples)):
            if "void" in self._mySamples[j]:
                self._ExemplarsVoid = j

        for k in range(len(self._mySamples)):
            if "samples" in self._mySamples[k]:
                self._ExemplarsEnd = k


        for i in range(len(self._mySamples)):
            if "samples" in self._mySamples[i]:
                self._SamplesStart = i+1
            
    
    def setExemplars (self):
        '''
        For each Exemplar in the file creates an object of type Alien and sets a list with all of them
        The Alien is created with Id and its characteristics in a list of ints
        Creates a list with all the Exemplars
        '''
        feature_vector=[]
        name_list = []
        self._Exemplars = []
        if "void" not in self._mySamples[self._ExemplarsVoid]:
            for exemplars in self._mySamples[constants.HEADER_TOTAL_LINES : self._ExemplarsEnd]:
                if "#List of samples:" not in exemplars:
                    self._exemplarsList.append(exemplars.replace('\n',''))
                    
            ##Creates the list with all the caracteristics of the Exemplar in int
            for i in range(len(self._exemplarsList)):
                self._exemplarsList[i]=self._exemplarsList[i].split(";")
                for k in range(constants.FEATURE_VECTORSTART, len(self._exemplarsList[i])):
                    self._exemplarsList[i][k]= int(self._exemplarsList[i][k])
                    vector = self._exemplarsList[i][constants.FEATURE_VECTORSTART:]
                feature_vector.append(vector)
            ##Creates a list with all the Ids        
            for i in range(len(self._exemplarsList)):
                for k in range(len(self._exemplarsList[i])):
                    Id = self._exemplarsList[i][0]
                name_list.append(Id)

            ##Creates a list with all the Exemplars of type Alien        
            for i in range ( len(self._exemplarsList)):
                alien = Alien(name_list[i], feature_vector[i])
                self._Exemplars.append(alien)

        else:
            self._exemplarsList.append(self._mySamples[self._ExemplarsVoid].replace('\n', ''))
        
    def setSamples(self):
        '''
        For each Sample in the file creates an object of type Alien and sets a list with all of them
        The Alien is created with Id and its characteristics in a list of ints
        Creates a list with all the Samples
        '''
        feature_vector=[]
        name_list = []
        self._Samples = []

        for i in range(self._SamplesStart, len(self._mySamples)):
            self._samplesList.append(self._mySamples[i])
        ##Creates the list with all the caracteristics of the Sample in int    
        for i in range(len(self._samplesList)):
            self._samplesList[i]=self._samplesList[i].split(";")
            for k in range(constants.FEATURE_VECTORSTART, len(self._samplesList[i])):
                self._samplesList[i][k]= int(self._samplesList[i][k])
                vector = self._samplesList[i][constants.FEATURE_VECTORSTART:]
            feature_vector.append(vector)
        ##Creates a list with all the Ids    
        for i in range(len(self._samplesList)):
            for k in range(len(self._samplesList[i])):
                name =self._samplesList[i][0]
            name_list.append(name)
        ##Creates a list with all the Samples of type Alien
        for i in range(len(self._samplesList)):
            alien = Alien (name_list[i], feature_vector[i])
            self._Samples.append(alien)

    def getExemplarsList (self):
        '''
        Gets the list of Exemplars in the inputFile
        '''
        return self._exemplarsList

    def getSamplesList (self):
        '''
        Gets the list of Samples in the inputFile
        '''
        return self._samplesList
        
    def getAlienExemplars(self):
        """
        Gets the list with the Exemplars of type Aliens in the inputFile
        """
        return self._Exemplars

    def getAlienSamples(self):
        '''
        Gets the list with the Samples of type Aliens in the inputFile
        '''
        return self._Samples 



