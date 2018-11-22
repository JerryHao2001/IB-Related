# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 15:30:25 2018

@author: 11658
"""

class Queue():
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self,n):
        self.items.append(n)
    def dequeue(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
        
if __name__ == '__main__':
    myQueue = Queue()
    print(myQueue.isEmpty())
    myQueue.enqueue(3)
    print(myQueue)
    print(myQueue.size())
    print(myQueue.dequeue())
    print(myQueue.isEmpty())
    
def hotPotato(nameList,num):
    temp = Queue()
    for i in nameList:
        temp.enqueue(i)
    while temp.size() > 1:
        for i in range(num):
            temp.enqueue(temp.dequeue())
        temp.dequeue()
    return temp   

    print(hotPotato(['A','B','C','D','E','F','G'],7))
if __name__ == '__main__':
    myQueue = Queue()
    print(myQueue.isEmpty())
    myQueue.enqueue(3)
    print(myQueue)
    print(myQueue.size())
    print(myQueue.dequeue())
    print(myQueue.isEmpty())
    
    print(hotPotato(['A','B','C','D','E','F','G'],7))
    
