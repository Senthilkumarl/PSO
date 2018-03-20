
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""

import numpy as np

def max_vec(vec, scal):    
    for i in range(len(vec)):        
        if vec[i] <  scal:
            vec[i] =scal
    return vec
            
    #return np.asarray([max(v,scal) for v in vec])

def min_vec(vec, scal):    
    for i in range(len(vec)):        
        if vec[i] >  scal:
            vec[i] =scal
    return vec

def boundary(vec, lowr, upr):
    for i in range(len(vec)):        
        if vec[i] <  lowr:
            vec[i] =lowr
        if vec[i] >  upr:
            vec[i] =upr
    return vec
def flip(v):
    if v == 1:
        return 0
    else:
        return 1

    
    
if __name__ == '__main__':
    vec=np.array([1,1,1,2,3,4,5,8])
    #print(max_vec(vec, 3))
    #print(min_vec(vec, 3))
    print(boundary(vec, 2, 5))
    print([flip(v) for v in [1.0,1,0.0,0,1]])
   
        