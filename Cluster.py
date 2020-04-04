# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo

class Cluster(object):
    """
    Cluster of examples
    """
    
    def __init__(self, examples, exampleType):
        """
        Constructor

        Requires:
        examples is a list of objects of a type that has
        a method returning the list of features of an object and
        a method returning the distance among them;
        exampleType string with type of examples
        Ensures:
        object of type Cluster is created
        """
        self._examples = examples
        self._exampleType = exampleType
        self._centroid = self.computeCentroid()


    def getExamples(self):
        """
        Examples in the cluster

        Ensures:
        list with examples in the cluster
        """
        return self._examples


    def getExampleType(self):
        """
        Type of examples in the cluster

        Ensures:
        type of examples
        """
        return self._exampleType


    def getCentroid(self):
        """
        Centroid of the cluster

        Ensures:
        centroid of the cluster
        """
        return self._centroid

            
    def size(self):
        """
        Size of the cluster

        Ensures:
        number of examples in cluster
        """
        return len(self._examples)


    def members(self):
        """
        Generator method
        """
        for e in self._examples:
            yield e


    def variance(self):
        """
        Variance

        Ensures:
        variance of the cluster
        """

        totDist = 0.0
        for e in self._examples:
            totDist += (e.distance(self._centroid))**2
        return totDist**0.5


    def computeCentroid(self):
        """
        Compute centroid of the cluster

        Ensures:
        centroid of the cluster
        """
        dim = self._examples[0].dimensionality()
        totVals = [0]*dim
        for e in self._examples:
            for i in range(dim):
                totVals[i] = totVals[i]+e.getFeatures()[i]
        totValsAveraged = []
        for i in range(dim):
            totValsAveraged.append(totVals[i]/float(len(self._examples)))
        centroid = self._exampleType('centroid', totValsAveraged)
        return centroid


    def update(self, examples):
        """
        Update the cluster with a given collection of examples

        Requires:
        examples a list of objects of type getExampleType()
        Ensures:
        examples = getExamples();
        returns how much the centroid has changed
        """
        oldCentroid = self._centroid
        self._examples = examples
        if len(examples) > 0:
            self._centroid = self.computeCentroid()
            return oldCentroid.distance(self._centroid)
        else:
            return 0.0

    def setExemplar(self):
        """
        calculates the distance between each Alien in the cluster and the centroid of that cluster and sets
        the one whos closest
        """
        ##Calculates the distace of the first Alien to the cluster's centroid 
        distance = self.getExamples()[0].distance(self.getCentroid())
        closest = None
        for example in self.getExamples():
            #compares the distance between each Alien in the Cluster and its Centroid and if the distance is
            #smaller sets him as the closest
            if int(example.distance(self.getCentroid())) <= distance:
                closest = example
                distance = example.distance(self.getCentroid())
        self._exemplar = closest

    def getExemplar(self):
        """
        gets the closest Alien to the centroid
        """
        return self._exemplar

    
    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form
        "Cluster with centroid [...] contains:
         ex1 ex2 ... exN "
        """
        
        names = []
        for e in self._examples:
            names.append(e.getName())
        names.sort()
        result = str(self._centroid.getFeatures())
        for e in names:
            result = result + e + ', '
        return result[:-2]
