
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:21:09 2018

@author: Senthilkumar Lakshmanan
"""
import numpy as np
from numpy.random import rand
import pickle

class particle:
    def __init__(self):
        self.Position = []
        self.Velocity = []
        self.Cost = np.Infinity
        self.Best = {'Position':[],'Cost':np.Infinity}
        self.isBest = False
        
    def updatePbest(self):
        if self.Cost < self.Best['Cost']:
            self.Best['Position'] = self.Position.copy()
            self.Best['Cost'] = self.Cost
            return True
        else:
            return False
        
    def updateGbest(self,GlobalBest_Cost, GlobalBest_Postion):
        if self.Best['Cost'] < GlobalBest_Cost:                    
            GlobalBest_Postion=self.Best['Position'].copy()
            GlobalBest_Cost= self.Best['Cost']
        return GlobalBest_Cost, GlobalBest_Postion.copy()
    
    def updateVelocity(self,GlobalBest_Postion,c1,c2,w,nVar):
        self.Velocity = w*self.Velocity \
            + c1*rand(nVar)*(self.Best['Position'] - self.Position) \
            + c2*rand(nVar)*(GlobalBest_Postion - self.Position)
        
        
def saveVars(data1):
    
    
    output = open('data.pkl', 'wb')
    
    # Pickle dictionary using protocol 0.
    pickle.dump(data1, output)
    

    output.close()
            
def loadVars():  
    
    pkl_file = open('data.pkl', 'rb')
    
    p = pickle.load(pkl_file)
    #pprint.pprint(data1)
    
   
    
    pkl_file.close()