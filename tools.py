

import numpy as np
from numpy.random import rand
# import matplotlib.pyplot as plt


def max_vec(vec, scal):
    #print(np.size(vec, 1))
    for i in range(np.size(vec, 1)):
        #print(i, vec[0,i])
        if vec[0,i] <  scal:
            vec[0,i] =scal
    return vec
            
    #return np.asarray([max(v,scal) for v in vec])

def min_vec(vec, scal):
    #print(type(vec))
    for i in range(np.size(vec, 1)):
        #print(i, vec[0,i])
        if vec[0,i] >  scal:
            vec[0,i] =scal
    return vec
    
    
if __name__ == '__main__':
    vec=np.array([[1,1,1,2,3,4,5,8]])
    #print(max_vec(vec, 3))
    print(min_vec(vec, 3))
   
        