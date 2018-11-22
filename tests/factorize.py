# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:41:34 2018

@author: 11658
"""
from math import log
def factorize(n):
    temp = []
    for i in range(int(log(n,2))+1):
        for j in range(2,n+1):            
            if n%j == 0:
                temp.append(str(j))
                n = int(n/j)
                break
    result = '*'.join(temp)
    return(result)
    
if __name__ == '__main__':
    print(factorize(7))
    print(factorize(8))
    print(factorize(1024))
    print(factorize(5675))
    print(factorize(1234498435))
            