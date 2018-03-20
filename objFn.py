
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""

import numpy as np

def sphere(x):
    x=np.asarray(x)
    
    return sum((x**2).tolist())

def sumn(x):
    x=np.asarray(x)
    
    return sum(x.tolist())
    