'''
Created on 23 mar. 2020

@author: a
'''
import math

import numpy as np 


MIN = -5
MAX = 5

def modularity(communities,param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']  
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat[i][j] - degrees[i] * degrees[j] / M)
    return Q * 1 / M