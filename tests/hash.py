# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 23:37:39 2018

@author: 11658
"""

class Hash():
    def __init__(self,size = 11):
        self.size = size
        self.slots = [None] * self.size
        self.value = [None] * self.size
        
    def assign(self,index,value):
        hashValue = self.value2hash(index,len(self,size))
        
        
    def get(self,index):
    
    
    
    
    def value2hash(self,key,size):
        return key%size
        
        
        
    def ():
        
        
    def __getitem__(self,index):
        self.get(index)
        
        
        
    def __setitem__(self,index,value):
        self.assign(index,value)