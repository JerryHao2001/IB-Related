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
    




def yes(ques):
    ans = input(ques).lower()
    return ans[0] == "y"

def animal():
    # Start with a singleton
    root = Tree("bird")

    # Loop until the user quits
    while True:
        print()
        if not yes("Are you thinking of an animal? "): break

        # Walk the tree
        tree = root
        while tree.left is not None:
            prompt = tree.cargo + "? "
            if yes(prompt):
                tree = tree.right
            else:
                tree = tree.left

        # Make a guess
        guess = tree.cargo
        prompt = "Is it a " + guess + "? "
        if yes(prompt):
            print("I rule!")
            continue

        # Get new information
        prompt  = "What is the animal's name? "
        animal  = input(prompt)
        prompt  = "What question would distinguish a {0} from a {1}? "
        question = input(prompt.format(animal, guess))

        # Add new information to the tree
        tree.cargo = question
        prompt = "If the animal were {0} the answer would be? "
        if yes(prompt.format(animal)):
            tree.left = Tree(guess)
            tree.right = Tree(animal)
        else:
            tree.left = Tree(animal)
            tree.right = Tree(guess)
            
        





if __name__ == "__main__":    
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

