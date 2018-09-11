# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 15:53:58 2018

@author: 11658
"""
def multiTable(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(str(j)+"X"+str(i)+'='+str(i*j),end = ' ')
        print('')
multiTable(9)

def multiTable1(n):
    i = 1
    while i <= n:
        j = 1
        while j <= i:
            print(str(j)+"X"+str(i)+'='+str(i*j),end = ' ')
            j+=1
        print('')
        i+=1
multiTable1(9)
