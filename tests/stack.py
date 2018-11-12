# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 23:20:25 2018

@author: 11658
"""

class stack(object):
    def __init__(self):
        self.item = []
        
    def push(self,n):
        self.item.append(n)
        
    def pop(self):
        self.item.pop()
        
    def isEmpty(self):
        return len(self.item) == 0
    
    def getSize(self):
        return len(self.item)
    
    def __str__(self):
        return('{}'.format(self.item))
    
if __name__ == '__main__':
    myStack = stack()
    print(myStack.getSize())
    myStack.push(1)
    print(myStack)
    myStack.push(2)
    print(myStack)
    myStack.pop()
    print(myStack)
    myStack.pop()
    print(myStack.isEmpty())