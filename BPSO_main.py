# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""

import objFn
import PSO
import numpy as np
import BPSO
import matplotlib.pyplot as plt

if __name__=='__main__':
    
    
    #================================Problem definition===========================================
      
    prob_prams = {
                  'nVar' : 50, #Number of unknown variable                  
                  'costFn': objFn.sumn
                  }
    
    #===========================================================================
    #===================================Parameters of PSO========================================
    
    pso_prams = {
                  'MaxIt' : 200, # Maximum number of iteration
                    'nPop' : 30, # Number of particle 
                    'w' : 1, #Inertia coefficient
                    'wdamp' : 0.95, #Damping ratio
                    'c1' : 2,
                    'c2' : 2 ,
                    'trans_fn': 8,
                    'Vmax':6,
                    "showItr":False
                  }
    #===========================================================================
    
    out_pso = BPSO.BPSO(prob_prams,pso_prams)     
    BestCosts = out_pso['BestCosts']
    GlobalBest = out_pso['GlobalBest']
    gbests =out_pso['gbests']
    p=out_pso['particle']
    print(GlobalBest)
    
    
    #     loadVars()
    #===========================================================================
    
    plt.semilogy(BestCosts)
    
    #     plt.plot(BestCosts)
    plt.xlabel('Iterations')
    plt.ylabel('cost value')
    plt.show()
