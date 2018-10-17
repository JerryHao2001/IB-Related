# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 22:19:43 2018

@author: 11658
"""

class point:
    '''
    a class represent a point with x,y coordinates
    '''
    
    def __init__(self,initX,initY):
        self.x = initX
        self.y = initY
    def getX(self):
        '''
        get the x coordinate
        '''
        return self.x
    def getY(self):
        '''
        get the y coordinate
        '''
        return self.y
    def __str__(self):
        '''
        print()
        (x,y)
        '''
        return "("+str(self.x)+','+str(self.y)+")"
    def __add__(self,other):
        '''
        return a point(x1+x2,y1+y2)
        '''
        newPoint = point(self.x+other.x,self.y+other.y)
        return newPoint
        