
import numpy as np
from numpy.random import rand
import objFn
import matplotlib.pyplot as plt
import tools

class partcle:
    def __init__(self):
        self.Position = []
        self.Velocity = 0
        self.Cost = 0
        self.Best = {'Position':[],'Cost':[]}
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
    MaxVelocity = 0.2*(varMax-varMin);
    MinVelocity = -MaxVelocity;
    #===========================================================================
     #=================================Initialization==========================================
    GlobalBest ={ 'Position':[],'Cost' : np.Infinity }
    p = [partcle() for i in range(0,nPop)]
    for i in range(0,nPop):
        #Generate random position
        p[i].Position = np.random.uniform(varMin,varMax,varSize)[0]
        #Initialize velocity
        p[i].Velocity = np.zeros(varSize)
        #Evoluation
       
        p[i].Cost = costFn(p[i].Position)
        #Update personal best
        p[i].Best['Position'] = p[i].Position
        p[i].Best['Cost'] = p[i].Cost 
        #Update Global Best        
        if p[i].Best['Cost'] < GlobalBest['Cost']:
            GlobalBest = p[i].Best
    BestCosts = [0]*MaxIt 

    for it in range(MaxIt):
        for i in range(nPop):
            p[i].Velocity = w*p[i].Velocity +   c1*rand(nVar)*(p[i].Best['Position'] - p[i].Position) + c2*rand(nVar)*(GlobalBest['Position'] - p[i].Position)
            #x=p[i].Best['Position'].tolist()
            #print(GlobalBest['Position'] ,GlobalBest['Position'].tolist()[3])
            # Update Position
            #Update Position and Cost
            #print(i,p[i].Velocity )
#             p[i].Velocity = tools.min_vec(p[i].Velocity,MaxVelocity)
#             p[i].Velocity = tools.min_vec(p[i].Velocity,MinVelocity)
            #print(MaxVelocity )
            p[i].Position = np.asarray(p[i].Position) + p[i].Velocity;
            p[i].Position  = np.asarray(tools.max_vec(p[i].Position,varMin))
            p[i].Position  = np.asarray(tools.min_vec(p[i].Position,varMax))
            
#             print(i,p[i].Position)
#             print(np.asarray(tools.max_vec(p[i].Position,varMin)))
#             print(np.asarray(tools.min_vec(p[i].Position,varMax)))
            #p[i].Position = np.asarray(tools.min_vec(p[i].Position[0],varMax))
            
#             print(i,p[i].Position)
#             print(tools.max_vec(p[i].Position[0],varMin))
#             print(tools.min_vec(p[i].Position[0],varMax))
            p[i].Cost = costFn(p[i].Position[0])
            #Update particle best and global best
            if p[i].Cost < p[i].Best['Cost']:
                p[i].Best['Position'] = p[i].Position
                p[i].Best['Cost'] = p[i].Cost 
                if p[i].Best['Cost'] < GlobalBest['Cost']:
                    GlobalBest = p[i].Best
            BestCosts[it] = GlobalBest['Cost']
        if pso_prams['showItr']:
            print("Iteration", it, 'Best cost', BestCosts[it] )
            
            #Damping  Inertia Coefficient
        w = w*wdamp
    out_pso = {
               'BestCosts' : BestCosts,
               'GlobalBest' : GlobalBest,
               'particle': p
               }
    return out_pso


# if __name__=='__main__':
#     #================================Problem definition===========================================
#       
#     prob_prams = {
#                   'nVar' : 5, #Number of unknown variable
#                   'varSize':[1,5],
#                   'varMin':-10 ,#Lower bounds of decision variable
#                   'varMax':10 ,#Upper bound of the decision variable
#                   'costFn': objFn.sphere
#                   }
#     
#     #===========================================================================
#     #===================================Parameters of PSO========================================
#    
#     pso_prams = {
#                   'MaxIt' : 100, # Maximum number of iteration
#                     'nPop' : 50, # Number of particle 
#                     'w' : 1, #Inertia coefficient
#                     'wdamp' : 0.8, #Damping ratio
#                     'c1' : 2,
#                     'c2' : 2 ,
#                     "showItr":True
#                   }
#     #===========================================================================
#     
#     out_pso = PSO(prob_prams,pso_prams)     
#     BestCosts = out_pso['BestCosts']
#     GlobalBest = out_pso['GlobalBest']
#     print(GlobalBest)
#     
#     #===========================================================================
#     
#     #plt.semilogy(BestCosts)
#     #plt.close('all')
#     plt.plot(BestCosts)
#     plt.xlabel('Iterations')
#     plt.ylabel('Iterations')
#     plt.show()
    
    
    
    