# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:19:50 2018

@author: 11658
"""

import matplotlib.pyplot as plt
import numpy as np
import random
import copy

class Schelling:
    def __init__(self, similarityThreshold = 30 , width = 10, height = 10, redBlue = 50, emptyRate = 10,  generation = 50 , races = 2):
        self.similarityThreshold = similarityThreshold
        self.width = width 
        self.height = height 
        self.races = races
        
        self.emptyRate = emptyRate
        self.emptyNum = int(width*height*emptyRate/100)
        
        self.redBlue = redBlue
        self.occupyNum = width * height-self.emptyNum
        self.redNum = int(self.occupyNum * redBlue/100)
        self.blueNum = int(self.occupyNum - self.redNum)
        
        
        self.generation = generation
        
        self.city = np.zeros([self.width,self.height])
        self.empty_houses = []
        self.agents = {}


    def initCity(self):
        zero = [0 for i in range(self.emptyNum)]
        one = [1 for i in range(self.redNum)]
        two = [2 for i in range(self.blueNum)]
        city = zero+one+two
        np.random.shuffle(city)
        self.city = np.reshape(np.array(city),(self.height,self.width))
                    
            
    def is_unsatisfied(self, x, y):
        pass
    def update(self):
        pass
    def move_to_empty(self, x, y):
        pass
    def plot(self, title, file_name):
        pass
    
jelly = Schelling()
jelly.initCity()