# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 00:26:30 2019

@author: 11658
"""
import numpy as np
from scipy.optimize import fsolve
import math

def f(x):
    Q1 = x[0]
    Q2 = x[1]
    Q3 = x[2]
    k =  x[3]
    def interfunc(a,b):
        return ((a-35)**2+(b-54)**2)**0.5
    #if 0< Q1 <= 1 and 0< Q2 <= 1 and 0< Q3 <= 1 and k > 0:
    if Q1>0 and Q2>0 and Q3>0 and k > 0:
        return [2*(Q1 / (4*math.pi*k*interfunc(37,56))+ Q2 / (4*math.pi*k*interfunc(37,56) )+ Q3 / (4*math.pi*k*interfunc(37,56)))-1.05733818472152 , 2*(Q1 / (4*math.pi*k*interfunc(51,60))+ Q2 / (4*math.pi*k*interfunc(51,60) )+ Q3 / (4*math.pi*k*interfunc(51,60)))-0.996092431821309 , 2*(Q1 / (4*math.pi*k*interfunc(65,51 ))+ Q2 / (4*math.pi*k*interfunc(65,51 ) )+ Q3 / (4*math.pi*k*interfunc(65,51 )))-0.859157032871277 , 2*(Q1 / (4*math.pi*k*interfunc(41,59))+ Q2 / (4*math.pi*k*interfunc(41,59) )+ Q3 / (4*math.pi*k*interfunc(41,59)))-1.06701523862376
            ]
    else:
        return [1,1,1,1]


print(['38 54 1.04726782953068','54  56  0.928333748786477','69  40 0.819235300710648','49 21 0.105475684918615'])

result = fsolve(f, np.array([1,1,1,1]))

print (result)
print (f(result))
