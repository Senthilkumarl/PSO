# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 16:25:34 2018

@author: senthilkumar
"""


import numpy as np
from numpy.random import rand
from random import random
import objFn
import math
from math import exp, pi, atan
import matplotlib.pyplot as plt
import tools

class partcle:
    def __init__(self):
        self.Position = []
        self.Velocity = 0
        self.Cost = 0
        self.Best = {'Position':[],'Cost':np.Infinity}
        self.isBest = False

def PSO(prob_prams, pso_prams):
    #================================Problem definition===========================================
     nVar=prob_prams['nVar']
     varSize=prob_prams['varSize']
     varMin=prob_prams['varMin']
     varMax=prob_prams['varMax']
     costFn=prob_prams['costFn']
     
     
     #===========================================================================
     #===================================Parameters of PSO========================================
    
     MaxIt = pso_prams['MaxIt'] # Maximum number of iteration
     nPop = pso_prams['nPop'] # Number of particle 
     w = pso_prams['w']; #Inertia coefficient
     wdamp = pso_prams['wdamp'] #Damping ratio
     c1 =pso_prams['c1'];
     c2 = pso_prams['c2']   
     wMax = pso_prams['wMax']      #Max inirtia weight
     wMin = pso_prams['wMin']      #Min inirtia weight
     Vmax = pso_prams['Vmax']
     MaxVelocity = 0.2*(varMax-varMin);
     MinVelocity = -MaxVelocity;
     #===========================================================================
      #=================================Initialization==========================================
     gBest ={ 'Position':[],'Cost' : np.Infinity }
     p = [partcle() for i in range(0,nPop)]
     for i in range(0,nPop):
         #Generate random position
         p[i].Position = np.random.randint(2, size=nVar)#np.random.uniform(varMin,varMax,varSize)[0]
         #Generate Binary random variable
         
         #Initialize velocity
         p[i].Velocity = np.zeros(nVar)
         #Evoluation
        
         p[i].Cost = costFn(p[i].Position)
         #Update personal best
         p[i].Best['Position'] = p[i].Position
         p[i].Best['Cost'] = p[i].Cost 
         #Update Global Best        
         if p[i].Best['Cost'] < gBest['Cost']:
             gBest = p[i].Best
     BestCosts = [0]*MaxIt 
     
     for it in range(MaxIt):
         for i in range(nPop):
             for j in range(nVar):
                 p[i].Velocity[j] = w*p[i].Velocity[j] \
                 + c1*random()*(p[i].Best['Position'][j]- p[i].Position.tolist()[j])\
                 + c2*random()*(gBest['Position'][j] - p[i].Position.tolist()[j])
                 
                 if p[i].Velocity[j] > Vmax:
                     p[i].Velocity[j] = Vmax
                 if p[i].Velocity[j] < -Vmax:
                     p[i].Velocity[j] = -Vmax
                 
                 
                 
                 s = abs((2/pi)*atan((pi/2)*p[i].Velocity[j]))
                 
                 if random()<s:
                     p[i].Position[j] = abs(min(2*p[i].Position.tolist()[j]-1,0))
                     
                 #print(p[i].Position[j])
                 
             p[i].Cost = costFn(p[i].Position)
             #Update particle best and global best
             if p[i].Cost < p[i].Best['Cost']:
                 p[i].Best['Position'] = p[i].Position
                 p[i].Best['Cost'] = p[i].Cost 
                 if p[i].Best['Cost'] < gBest['Cost']:
                     gBest = p[i].Best
             BestCosts[it] = gBest['Cost']
             if pso_prams['showItr']:
                 print("Iteration", it, 'Best cost', BestCosts[it] )
                 
                 #Damping  Inertia Coefficient
             #w=wMax-it*((wMax-wMin)/MaxIt)
     w = w * wdamp;
     out_pso = {
               'BestCosts' : BestCosts,
               'GlobalBest' : gBest,
               'particle': p
               }
     return out_pso
    
     


if __name__=='__main__':
#     #================================Problem definition===========================================
#   
    
    prob_prams = {
                  'nVar' : 5, #Number of unknown variable
                  'varSize':[1,5],
                  'varMin':-10 ,#Lower bounds of decision variable
                  'varMax':10 ,#Upper bound of the decision variable
                  'costFn': objFn.sphere#objFn.sumn
                  }
    #     
    #     #===========================================================================
    #     #===================================Parameters of PSO========================================
    #
    
    pso_prams = {
                  'MaxIt' : 100, # Maximum number of iteration
                    'nPop' : 50, # Number of particle 
                    'w' : 1, #Inertia coefficient
                    'wdamp' : 0.8, #Damping ratio
                    'c1' : 2,
                    'c2' : 2 ,
                    'wMax':0.9,         #Max inirtia weight
                    'wMin':0.4,         #Min inirtia weight
                    'Vmax':6,
                    "showItr":True
                }
       
    out_pso = PSO(prob_prams,pso_prams)     
  
    
    BestCosts = out_pso['BestCosts']
    GlobalBest = out_pso['GlobalBest']
    print(GlobalBest)
     
    #===========================================================================
     
    #plt.semilogy(BestCosts)
    #plt.close('all')
    plt.plot(BestCosts)
    plt.xlabel('Iterations')
    plt.ylabel('Iterations')
    plt.show()