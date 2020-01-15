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
    showTreePost(tree.left)
    showTreePost(tree.right)
    print(tree.cargo,end = ' ')

def showTreeIn(tree):
    if tree == None: return 
    showTreeIn(tree.left)
    print(tree.cargo,end = ' ')
    showTreeIn(tree.right)

def showTreePre(tree):
    if tree == None: return 
    print(tree.cargo,end = ' ')
    showTreePre(tree.left)
    showTreePre(tree.right)
    
    

if __name__ == "__main__":    
    jelly = Tree('83',Tree('79',Tree('76'),Tree('75')),Tree('72',Tree('70'),Tree('68')))
    
    print('Post')
    showTreePost(jelly)
    print('\n')
    print('in')
    showTreeIn(jelly)
    print('\n')
    print('Pre')
    showTreePre(jelly)
    print('\n')
    


