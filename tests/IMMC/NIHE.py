# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 15:51:31 2019

@author: 11658
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
from mpl_toolkits.mplot3d import Axes3D


def func(x, Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3):
    p1 = np.array([m1,n1])
    p2 = np.array([m2,n2])
    p3 = np.array([m3,n3])    
    return (Q1 / 4*math.pi*k) * (1 / (np.square(x-p1).sum())**0.5) + (Q2 / 4*math.pi*k) * (1 / (np.square(x-p2).sum())**0.5) + (Q3 / 4*math.pi*k) * ((1 / (np.square(x-p3).sum())**0.5))
#定义x、y散点坐标
#x = [20,30,40,50,60,70]
x = np.array([[24,56],[33,67],[12,89],[84,28],[45,67],[23,45],[87,34],[12,45],[63,46],[4,92]])
num = [0.82,0.79,0.02,0.25,0.98,0.70,0.37,0.41,0.80,0.00]
y = np.array(num)
#非线性最小二乘法拟合
popt, pcov = curve_fit(func, x, y)
#获取popt里面是拟合系数
print(popt)

Q1 = popt[0]
Q2 = popt[1]
Q3 = popt[2]
k = popt[3]
m1 = popt[4]
n1 = popt[5]
m2 = popt[6]
n2 = popt[7]
m3 = popt[8]
n3 = popt[9]
'''
yvals = func(x, Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3) #拟合y值
print('popt:', popt)


print('系数pcov:', pcov)
print('系数yvals:', yvals)
#绘图
fig = plt.figure()
ax = Axes3D(fig)
X = np.arange(0,101)
Y = np.arange(0,101)
X, Y = np.meshgrid(X, Y)
yvals = np.meshgrid(yvals)
ax.plot_surface(X, Y, yvals, rstride=1, cstride=1, cmap='rainbow')
plt.show()
'''