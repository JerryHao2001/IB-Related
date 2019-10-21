# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 17:05:17 2019

@author: 11658
"""

import xlrd
import numpy as np
import math
from scipy.optimize import curve_fit

data=xlrd.open_workbook("data.xlsx")
table=data.sheets()[0]
data=[]
for i in range(2,103):
    temp = table.row_values(i,2,103)
    data += temp
Y = np.array(data)#.reshape(10201,1)


x = []
for i in range(0,101):
    #x.append([])
    for j in range(0,101):
        x.append([j,i])
X = np.array(x,dtype = float)


def func1(x,k):
    Q = 982
    p1 = np.array([69,45])
    p2 = np.array([43,61])
    p3 = np.array([35,54])
    return 2*(Q / (4*math.pi*k*interSum(x,p1))+ Q / (4*math.pi*k*interSum(x,p2)) + Q / (4*math.pi*k*interSum(x,p3)))



def interSum(xx,p):

    t = np.zeros(len(xx),dtype = float)
    s=(xx-p)*1
    for i in range(len(s)):
        t[i] = (s[i][0]**2+s[i][1]**2)**0.5
    t[t==0]=1
    return t


popt, pcov = curve_fit(func1, X, Y , maxfev=100000,ftol = 10**-10)
k = popt[0]
yvals =  func1(X,k)