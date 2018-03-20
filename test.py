# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""
import numpy as np
from numpy.random import rand
from random import random
import objFn
import pprint, pickle
from math import exp, pi, atan, tanh, sqrt
import matplotlib.pyplot as plt
import tools

from swarm import *
    
    

def PSO(prob_prams, pso_prams):
    #================================Problem definition===========================================
    nVar=prob_prams['nVar']
    varSize=[1,prob_prams['nVar']]    
    costFn=prob_prams['costFn']
    varMin=prob_prams['varMin']
    varMax=prob_prams['varMax']
    
    #===========================================================================
    #===================================Parameters of PSO========================================
   
    MaxIt = pso_prams['MaxIt'] # Maximum number of iteration
    nPop = pso_prams['nPop'] # Number of particle 
    w = pso_prams['w']; #Inertia coefficient
    wdamp = pso_prams['wdamp'] #Damping ratio
    c1 =pso_prams['c1'];
    c2 = pso_prams['c2']  
    #Vmax = pso_prams['Vmax'];
    
    s = np.zeros(nVar)
    
    #===========================================================================
     #=================================Initialization==========================================
    GlobalBest_Postion=[]
    GlobalBest_Cost= np.Infinity
    
    p = [particle() for i in range(0,nPop)]
    for i in range(0,nPop):
        #Generate random position
        p[i].Position = np.random.uniform(varMin,varMax,nVar)
        #Initialize velocity
        p[i].Velocity = np.zeros(nVar)        
        
        #Update personal best
        p[i].Best['Position'] = p[i].Position.copy()
        p[i].Best['Cost'] = p[i].Cost 
        
        #Update Global Best      
        GlobalBest_Cost, GlobalBest_Postion = p[i].updateGbest(GlobalBest_Cost, GlobalBest_Postion)

            
    BestCosts = [0]*MaxIt 
    gbests = [0]*MaxIt 

# ===========================Evaluation Iteration begins here==============================================
    for it in range(MaxIt):        
        for i in range(nPop):    
            #Evaluate the cost function
            p[i].Cost = costFn(p[i].Position)


            if p[i].updatePbest():
                GlobalBest_Cost, GlobalBest_Postion = p[i].updateGbest(GlobalBest_Cost, GlobalBest_Postion)

            #Update Velocity
            p[i].updateVelocity(GlobalBest_Postion,c1,c2,w,nVar)
            
            
            #Update Position and Cost
            
            p[i].Position =p[i].Position + p[i].Velocity;
            p[i].Position = tools.boundary(p[i].Position, varMin, varMax) 
            
#           
        BestCosts[it] = GlobalBest_Cost
        gbests[it] = (GlobalBest_Postion,GlobalBest_Cost)
        
        
        
        if pso_prams['showItr']:
            print("Iteration", it, 'Best cost', BestCosts[it] )
            
            #Damping  Inertia Coefficient
        w = w*wdamp
        #----------------------------------------------------------------------------------------------
    out_pso = {
               'BestCosts' : BestCosts,
               'GlobalBest' : (GlobalBest_Postion,GlobalBest_Cost),
               'gbests' : gbests,
               'particle': p
               }
    return out_pso


if __name__=='__main__':    
    
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
    
    out_pso = PSO(prob_prams,pso_prams)     
    BestCosts = out_pso['BestCosts']
    GlobalBest = out_pso['GlobalBest']
    gbests =out_pso['gbests']
    p=out_pso['particle']
    print(GlobalBest)
    
    saveVars(gbests)
    #     loadVars()
    #===========================================================================
    
    #plt.semilogy(BestCosts)
    
    plt.plot(BestCosts)
    plt.xlabel('Iterations')
    plt.ylabel('cost value')
    plt.show()

    
    
    