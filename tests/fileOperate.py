# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:08:29 2018

@author: 11658
"""
'''
jellyFile = open('jellyFile.txt',"w")
jellyFile.write('testing\n')
jellyFile.write('Hello World')
jellyFile.close()
'''
myHandle = open('jellyFile.txt','r')
'''
a = myHandle.readline()
print(a)
'''
b= myHandle.readlines()
print(b)
b.sort()
print(b)