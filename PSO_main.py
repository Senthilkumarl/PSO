
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""

import objFn
import PSO
import numpy as np
import matplotlib.pyplot as plt

#================================Problem definition===========================================

prob_prams = {
            'nVar' : 10, #Number of unknown variable'varMin':-10 ,#Lower bounds of decision variable
        'varMin':-10 ,#Lower bounds of decision variable
        'varMax':10 ,#Upper bound of the decision variable
        'costFn': objFn.sphere
            }

#===========================================================================
#===================================Parameters of PSO========================================

pso_prams = {
        'MaxIt' : 100, # Maximum number of iteration
          'nPop' : 50, # Number of particle 
          'w' : 1, #Inertia coefficient
          'wdamp' : 0.8, #Damping ratio
          'c1' : 2,
          'c2' : 2 ,
          "showItr":False
        }
#===========================================================================

out_pso = PSO.PSO(prob_prams,pso_prams)     
BestCosts = out_pso['BestCosts']
GlobalBest = out_pso['GlobalBest']
gbests =out_pso['gbests']
p=out_pso['particle']
print(GlobalBest)


#     loadVars()
#===========================================================================

#plt.semilogy(BestCosts)

plt.plot(BestCosts)
plt.xlabel('Iterations')
plt.ylabel('cost value')
plt.show()