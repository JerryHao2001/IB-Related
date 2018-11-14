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
        return self.item.pop()
        
    def isEmpty(self):
        return len(self.item) == 0
    
    def getSize(self):
        return len(self.item)
    
    def __str__(self):
        return('{}'.format(self.item))
    
def reverseStr(n):
    assert type(n) == str ,'Only String'
    temp = stack()
    for i in n:
        temp.push(i)
    return(''.join([(temp.pop()) for i in range(temp.getSize())]))
    
def balancedParenthese(n):
    assert type(n) == str , 'Only String'
    temp = stack()
    front = ['(','[','{']
    back = [')',']','}']
    for i in n:
        if i in front:
            temp.push(i)           
        elif i in back:
            if temp.isEmpty():
                return False           
            elif front.index(temp.pop()) != back.index(i):
                return False
    return True if temp.isEmpty() else False
                
def de2bi(de):
    assert type(de) == int, "Only Int"
    temp = stack()
    while de > 0:
        temp.push(de%2)
        de //= 2
    return(''.join([(str(temp.pop())) for i in range(temp.getSize())]))
    
def de2he(he):
    digit = '0123456789ABCDEF'
    dic = {}
    temp = stack()
    for i in range(0,16):
        dic[i] = digit[i]
    while he > 0:
        temp.push(dic[he%16])
        he //= 16
    return (''.join([str(temp.pop()) for i in range(temp.getSize())]))
            
            

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
    print('\n')
    print(reverseStr('jelly'))
    print(balancedParenthese('([])'))
    print(balancedParenthese('{[()]}'))
    print(balancedParenthese(')'))
    print('\n')
    print(de2bi(10))
    print(de2bi(2048))
    print(de2he(31))
    print(de2he(256))