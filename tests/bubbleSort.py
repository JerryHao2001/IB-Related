# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:58:56 2018

@author: 11658
"""

def bubbleSort(n):
    """
    input: list n
    output: sorted list n
    """
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                n[j],n[j+1] = n[j+1],n[j]
        print(n)
    return(n)