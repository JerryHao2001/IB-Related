# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 08:35:27 2018

@author: 11658
"""
import numpy as np

def quiz1(k = 3,p = 1):
    while k > 1:
        print(k)
        k = k-1
        p = p*k
    else:
        print(p)
        
class magicSquare():
    def __init__(self,square):
        self.square = square
        self.n = len(self.square)
        
    def check(self):
        Sum = 0
        temp1 = 0
        for i in range(self.n):
            Sum += self.square[(self.n-1-i),i]  
            temp1 += self.square[i,i]
        if temp1 != Sum:
            return False
            
        for i in range(self.n):
            temp2 = 0
            temp3 = 0
            for j in range(self.n):
                temp2 += self.square[i,j]
                temp3 += self.square[j,i]
            if (temp2 != Sum) or (temp3 != Sum):
                return False
        return True
    def get(self,n = 5):
        '''
        n is the number of row of ur Square
        n must be odd
        '''
        assert n % 2 != 0,'n must be odd'
        newSquare = np.empty([n,n])
        x,y = 0,n//2
        allIndex = []
        for i in range(1,n**2+1):
            index = [x,y]
            allIndex.append(index)
            newSquare[x,y] = i
                   
            x_,y_ = x-1,y+1
            x_ = n-1 if x_ < 0 else x_
            x_ = 0 if x_ > n-1 else x_
            y_ = 0 if y_ > n-1 else y_
            
            (x,y) = (x+1,y) if ([x_,y_] in allIndex)  else (x-1,y+1)
            x = n-1 if x < 0 else x
            x = 0 if x > n-1 else x
            y = 0 if y > n-1 else y

        self.square = newSquare
            
            
            
        
        
            
            
        