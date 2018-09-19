# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 15:45:26 2018

@author: 11658
"""

def isIn(m,n):
    '''
    m,n are string
    if m includes n or n includes m - return True
    else - return False
    '''
    if len(m)>len(n):
        up,low = m,n
    else:
        up,low = n,m
    for i in range(len(up)-len(low)+1):
        if up[i:i+len(low)] == low:
            return True
    return False
                