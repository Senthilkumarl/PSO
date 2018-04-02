
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""
from random import random
import objFn
from math import exp, pi, atan, tanh, sqrt, erf
import matplotlib.pyplot as plt
import tools
import numpy as np
from swarm import *
    

def BPSO(prob_prams, pso_prams):
    #================================Problem definition===========================================
    nVar=prob_prams['nVar']
    #varSize=[1,prob_prams['nVar']]    
    costFn=prob_prams['costFn']
    
    
    #===========================================================================
    #===================================Parameters of BPSO========================================
   
    MaxIt = pso_prams['MaxIt'] # Maximum number of iteration
    nPop = pso_prams['nPop'] # Number of particle 
    w = pso_prams['w']; #Inertia coefficient
    wdamp = pso_prams['wdamp'] #Damping ratio
    c1 =pso_prams['c1'];
    c2 = pso_prams['c2']  
    Vmax = pso_prams['Vmax'];
    trans_fn = pso_prams['trans_fn']
    s = np.zeros(nVar)
    
    #===========================================================================
    #=================================Initialization==========================================
    GlobalBest_Postion=[]
    GlobalBest_Cost= np.Infinity
    
    p = [particle() for i in range(0,nPop)]
    for i in range(0,nPop):
        #Generate random position
        p[i].Position = np.random.randint(2, size=nVar)
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
            
            p[i].Velocity = tools.boundary(p[i].Velocity, -Vmax, Vmax) 
            #Update Position and Cost
            
            #Transfer functions
            for j in range(nVar): 
                if trans_fn == 1:
                    s[j] = 1/(1+exp(-2*p[i].Velocity[j])) 
                if trans_fn == 2:
                    s[j] = 1/(1+exp(-p[i].Velocity[j]))  
                if trans_fn == 3:
                    s[j] = 1/(1+exp(-p[i].Velocity[j]/2))  
                if trans_fn == 4:
                    s[j] = 1/(1+exp(-p[i].Velocity[j]/3))  
                    
                if trans_fn <= 4:
                    if random() < s[j]: 
                        p[i].Position[j] = 1
                    else:
                        p[i].Position[j] = 0
                if trans_fn == 5:
                    s[j] = abs(erf(((sqrt(pi)/2)*p[i].Velocity[j]))) 
                if trans_fn == 6:
                    s[j] = abs(tanh(p[i].Velocity[j])) 
                if trans_fn == 7:
                    s[j] = abs(p[i].Velocity[j]/sqrt((1+p[i].Velocity[j]**2))) 
                if trans_fn == 8:
                    s[j] = abs((2/pi)*atan((pi/2)*p[i].Velocity[j]))
                
                if trans_fn > 4:
                    if random() < s[j]:                                             
                        p[i].Position[j] = tools.flip(p[i].Position[j])

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
                  'nVar' : 50, #Number of unknown variable                  
                  'costFn': objFn.sumn
                  }
    
    #===========================================================================
    #===================================Parameters of PSO========================================
    plt.rc('text', usetex=True)
    plt.rc('font', family='serif')
    transFnStr = [
            r'$\frac{1}{1+e^{-2v}}$',
            r'$\frac{1}{1+e^{-v}}$',
            r'$\frac{1}{1+e^{-v/2}}$',
            r'$\frac{1}{1+e^{-v/3}}$',
            r'$\left|erf(\sqrt{\frac{\pi}{2}}v)\right|$',
            r'$\left|tanh(v)\right|$',
            r'$\left|\frac{v}{\sqrt{1+v^2}}\right|$',
            r'$\left|\frac{2}{\pi}atan\left(\left(\frac{\pi}{2}\right)v\right)\right|$'
            ]
    
    for n in range(0,8):
        pso_prams = {
                      'MaxIt' : 200, # Maximum number of iteration
                        'nPop' : 30, # Number of particle 
                        'w' : 1, #Inertia coefficient
                        'wdamp' : 0.95, #Damping ratio
                        'c1' : 2,
                        'c2' : 2 ,
                        'trans_fn': n,
                        'Vmax':6,
                        "showItr":False
                      }
        #===========================================================================
        
        out_pso = BPSO(prob_prams,pso_prams)     
        BestCosts = out_pso['BestCosts']
        GlobalBest = out_pso['GlobalBest']
        gbests =out_pso['gbests']
        p=out_pso['particle']
        print(GlobalBest)
        
        saveVars(gbests)
        #     loadVars()
        #===========================================================================
        print(transFnStr[n])
        #line1, = plt.semilogy(BestCosts, label='TF'+ str(n+1) +': ' + transFnStr[n])
        
        line1, = plt.plot(BestCosts, label='TF'+ str(n+1) +': ' + transFnStr[n])
        plt.xlabel('Iterations')
        plt.ylabel('Optimal cost')
    from matplotlib.legend_handler import HandlerLine2D
    plt.legend(handler_map={line1: HandlerLine2D(numpoints=8)}, loc=1, fontsize=12)
    plt.show()

    
    
    