

import numpy as np

def sphere(x):
    x=np.asarray(x)
    
    return sum((x**2).tolist())

def sumn(x):
    x=np.asarray(x)
    
    return sum(x.tolist())
    