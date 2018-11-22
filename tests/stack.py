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
    
def de2he(de):
    digit = '0123456789ABCDEF'
    dic = {}
    temp = stack()
    for i in range(0,16):
        dic[i] = digit[i]
    while de > 0:
        temp.push(dic[de%16])
        de //= 16
    return (''.join([str(temp.pop()) for i in range(temp.getSize())]))


'''            
from pythonds.basic.queue import Queue

import random

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numSeconds, pagesPerMinute):

    labprinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingtimes = []

    for currentSecond in range(numSeconds):

      if newPrintTask():
         task = Task(currentSecond)
         printQueue.enqueue(task)

      if (not labprinter.busy()) and (not printQueue.isEmpty()):
        nexttask = printQueue.dequeue()
        waitingtimes.append( nexttask.waitTime(currentSecond))
        labprinter.startNext(nexttask)

      labprinter.tick()

    averageWait=sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(10):
    simulation(3600,5)

'''

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