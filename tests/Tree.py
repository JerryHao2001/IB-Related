# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 15:35:25 2018

@author: 11658
"""
class Tree():
    def __init__(self,cargo,left = None,right = None):
        self.cargo = cargo
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.cargo)
    
def showTreePost(tree):
    if tree == None: return 
    print(tree.cargo,end = ' ')
    showTreePost(tree.left)
    showTreePost(tree.right)

def showTreeIn(tree):
    if tree == None: return 
    showTreeIn(tree.left)
    print(tree.cargo,end = ' ')
    showTreeIn(tree.right)

def showTreePre(tree):
    if tree == None: return 
    showTreePost(tree.left)
    showTreePost(tree.right)
    print(tree.cargo,end = ' ')



        
jelly = Tree('a',Tree('b',Tree('d'),Tree('e')),Tree('c',Tree('f',Tree('g'))))
h = Tree('+',Tree('1'),Tree('*',Tree('2'),Tree('3')))

showTreePost(jelly)
print('\n')
showTreeIn(jelly)
print('\n')
showTreePre(jelly)
print('\n')

showTreePost(h)
print('\n')
showTreeIn(h)
print('\n')
showTreePre(h)

