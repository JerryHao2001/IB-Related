# -*- coding: utf-8 -*-
"""
Created on Thu Nov 15 11:27:38 2018

@author: 11658
"""

class stack(object):
    def __init__(self):
        self.item = []
        
    def push(self,n):
        self.item.append(n)
        
    def pop(self):
        return self.item.pop()
        
    def isEmpty(self):
        return len(self.item) == 0
    
    def getSize(self):
        return len(self.item)
    
    def __str__(self):
        return('{}'.format(self.item))

def RPN(n):
    assert type(n) == str, "Only Str"
    temp = stack()    
    for i in n.split(' '):
        if i.isalnum():
            temp.push(i)
        else:
            if temp.getSize() == 1:
                return temp.pop()
            a = temp.pop()
            b = temp.pop()
            temp.push(str(eval(b+i+a)))
    return temp.pop()

def in2post(n):
    
    
    
if __name__ == '__main__':
    print(RPN('10'))
    print(RPN('2 8 *'))
    print(RPN('10 2 8 * + 3 -'))