# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 08:15:15 2018

@author: 11658
"""

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = self.newdata
    def setNext(self,newnext):
        self.next = newnext
    def __str__(self):
        return(str(self.data))
        
class unorderedList():
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head  == None


    def getSize(self):
        current = self.head
        count = 0
        while current != None:
            count += 1
            current = current.getNext()
        return count
    
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        
     
    
    def search(self,item):
        current= self.head
        found = False
        #temp = None
        while current != None and not found:
            if current.getData() == item :
                found = True
                #print('from',temp)
            else:
                #temp = current
                current = current.getNext()
        return found
    
    def index(self,item):
        current = self.head
        index = 0
        found = False
        while current != None and (not found):
            if current.getData() == item:
                found = True
            else: 
                current = current.getNext()
                index += 1
        if index > self.getSize()-1:
            return False
        else:
            return index
               
    def append(self,item):
        temp = Node(item)
        current  = self.head
        for i in range(self.getSize()-1):
            current = current.getNext()
        current.setNext(temp)
    
    def insert(self,position,item):
        temp = Node(item)
        current = self.head
        previous = None
        Next = current.getNext()
        if position == 0:
            self.add(item)
        elif position == self.getSize():
            self.append(item)
        else:
            for i in range(position):
                previous = current
                current = current.getNext()
                Next = current.getNext()
            temp.setNext(Next)
            previous.setNext(temp)
                
    def __str__():
        pass
        
            
        
jelly = unorderedList()
jelly.add(1)
jelly.add(2)
jelly.add(3)
jelly.add(4)  
        
    