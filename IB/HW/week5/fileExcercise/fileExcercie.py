# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:32:33 2018

@author: 11658
"""
def formJellyFile():
    """
    make original file
    """
    file = open('jellyFile.txt','w')
    file.write('Jelly\n')
    file.write('Hello\n')
    file.write('World\n')
    file.write('snake\n')
    file.close()


# Question1
def fileReverse():
    """
    reverse lines in the file
    """
    inFile = open('jellyFile.txt','r')
    outFile = open('jellyFileReverse.txt','w')
    temp = inFile.readlines()
    for i in range(len(temp)-1,-1,-1):
        outFile.write(temp[i])
    inFile.close()
    outFile.close()
    
# Question2
def fileFilter():
    """
    print lines including 'snake'
    """
    inFile = open('jellyFile.txt','r')
    temp = inFile.readlines()
    for i in temp:
        if 'snake' in i:
            print(i)

# Question3
def fileNumbered():
    """
    add number tags on the lines(0001,0002)
    """
    inFile = open('jellyFile.txt','r')
    outFile = open('jellyFileNumbered.txt','w')
    temp = inFile.readlines()
    for i in range(len(temp)):
        outFile.write("{:0>4d} ".format(i+1))
        outFile.write(temp[i])

# Question4
def fileUnNumbered():
    """
    delet number tages
    """
    inFile = open("jellyFileNumbered.txt",'r')
    outFile = open('jellyFileUnNumbered.txt','w')
    temp = inFile.readlines()
    for i in range(len(temp)):
        outFile.write(temp[i][5:])