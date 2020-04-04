# 2017-2018 Programacao II (LTI)
# Grupo 76
# 44366 Alexandre Vidal
# 51628 Tiago Robalo

class Alien(object):
    """
    Example for clusetring
    """


    def __init__(self, Id, features, label = None):
        """
        Constructor

        Requires:
        features is list of numbers representing the feature vector;
        label is string with the label of the example
        Ensures:
        object of type Example created
        """
        self._Id = Id
        self._features = features
        self._label = label


    def dimensionality(self):
        """
        Dimensionality of the feature vector

        Ensures:
        dimensionality of the feature vector
        """
        return len(self._features)


    def getFeatures(self):
        """
        Features

        Ensures:
        feature vector
        """
        return self._features[:]


    def getLabel(self):
        """
        Object label

        Ensures:
        object label
        """
        return self._label


    def getId(self):
        """
        Object Name

        Ensures:
        object name
        """
        return self._Id

    def minkowskiDist(self,v1, v2, p):
        """Minkowski distance

        Requires:
        v1 and v2 are equal-dimension arrays of numbers,
        p represents Minkowski order
        Ensures:
        Minkowski distance of order p between v1 and v2
        """
        dist = 0.0
        for i in range(len(v1)):
            dist += abs(v1[i] - v2[i])**p
        return dist**(1.0/p)



    def distance(self, other):
        """
        Euclidean distance wrt a given example

        Requires:
        other is an example
        Ensures:
        the Euclidean distance between feature vectors
        of self and other
        """
        return self.minkowskiDist(self._features, other.getFeatures(), 2)


    def __str__(self):
        """
        String representation

        Ensures:
        string representation in the form "name:features:label"
        """
        return self._name + ':' + str(self._features)



 
