#!/usr/bin/python

import random
import collections
import math
import sys

from numpy import argmin
from util import *

############################################################
# Problem 1: k-means
############################################################

def kmeans(examples, K, maxIters):
        '''
        examples: list of examples, each example is a string-to-double dict representing a sparse vector.
        K: number of desired clusters. Assume that 0 < K <= |examples|.
        maxIters: maximum number of iterations to run (you should terminate early if the algorithm converges).
        Return: (length K list of cluster centroids,
        list of assignments (i.e. if examples[i] belongs to centers[j], then assignments[i] = j)
        final reconstruction loss)
        '''
        # BEGIN_YOUR_CODE (our solution is 28 lines of code, but don't worry if you deviate from this)
        selections = random.choices(examples, k=K) #three random centroids x
        centroids = []
        assignments = []
        iters = 0

        vectors = []
        for i in examples:
                M = max(i, default=0)
                vectors.append([i.get(j,0) for j in range(M)])
        
        for i in selections:
                M = max(i, default=0)
                centroids.append([i.get(j,0) for j in range(M)])

        while iters != maxIters:
                assignments = []
                distances = [[0 for i in range(len(centroids))] for i in range(len(vectors))]
                for i, num in (vectors, range(len(vectors))):
                        for j in range(len(centroids)):
                                distances[num][j] =  sum([(x-x1)**2 for x, x1 in (vectors[i], centroids[j][i])])
                        assignments.append(distances[num].index(min(distances[num])))
                
                for j in range(K):
                        new_centroids = [0 for i in range(K)]
                        total_elem = 0
                                


        # END_YOUR_CODE
