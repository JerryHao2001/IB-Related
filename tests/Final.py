# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:53:47 2019

@author: 11658
"""
import numpy as np
import Tree

# Question 13
myArray = np.zeros([6,6])
myArray[0,0] = 7
myArray[2,2] = -3
myArray[2,4] = 9
myArray[4,2] = -1
myArray[5,1] = -6
myArray[5,4] = -5
myArray[5,5] = 1

def compress(myArray):
    values = []
    rowc = []
    col = []
    rowcCount = 0
    for i in myArray:
        for j in range(len(i)):
            if int(i[j]) != 0 :
                values.append(i[j])
                col.append(j)
                rowcCount += 1
        rowc.append(rowcCount)
    print(values)
    print(rowc)
    print(col)

#Question 10
myStack = ["alpha",'mu','gamma','delta','epsilon','zeta','lambda','theta']
myTree = Tree.Tree(myStack.pop())
'''
def treeConstruct(item,root):
    if root == None:
        root = Tree.Tree(item)
    elif item[0] < root.cargo[0]:
        #root.left = Tree.Tree(item)
        treeConstruct(item,root.left)
    elif item[0] > root.cargo[0]:
        treeConstruct(item,root.right)
        #root.right = Tree.Tree(item)

treeConstruct(myStack.pop(),myTree)

Tree.showTreeIn(myTree)
'''

def treeConstructIteration():
    global myStack, myTree
    item = myStack.pop()
    root = myTree
    finish = -1
    while finish == -1:     
        if item[0] < root.cargo:
            if root.left == None:
                root.left = Tree.Tree(item)
                finish = 1
            else:
                root = root.left
        elif item[0] > root.cargo:
            if root.right == None:
                root.right = Tree.Tree(item)
                finish = 1
            else:
                root = root.right
    Tree.showTreeIn(myTree)