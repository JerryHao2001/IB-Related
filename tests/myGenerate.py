# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 22:09:17 2018

@author: 11658
"""

class species():
    import numpy as np
    import matplotlib.pyplot as plt
    
    def __init__(self,DNALength = 10,popSize = 5,xRange = [0,5],crossRate = 0.8,mutateRate = 0.003):
        self.DNALength = DNALength 
        self.popSize = popSize   
        self.xRange = xRange
        self.crossRate = crossRate
        self.mutateRate = mutateRate
        self.population = np.random.randint(low = 0,high = 2,size = (self.popSize,self.DNALength))
   
    def translate(self):
        self.translated = (self.population.dot(np.arange(self.DNALength)[::-1] ** 2)) / (2 ** self.DNALength -1) * self.xRange[-1] 
        
    def getFitness(self):
        def f(x):
            return np.sin(10*x)*x + np.cos(2*x)*x   
        self.fitness = f(self.translated) + 10**(-10) - np.min(f(self.translated))

    def select(self):
        index = np.random.choice(a = np.arange(self.popSize),size = self.popSize,replace  = True,p = self.fitness / sum(self.fitness))
        self.population = self.population[index]
    
    def mute(self):#全群种交叉 
        
        def crossover(parent1,popCopy):
            if np.random.rand() < self.crossRate:
                #parent2 = popCopy[int(np.random.randint(low = 0,high = self.popSize,size = 1))]
                temp = np.random.randint(low = 0,high = self.popSize,size = 1)
                crossPoints = (np.random.randint(low = 0,high =  2, size = self.DNALength)).astype(np.bool)
                parent1[crossPoints] = popCopy[temp,crossPoints]
            return parent1
            
        def mutate(child):
            for i in range((self.DNALength)):
                if np.random.rand() < self.mutateRate:
                    child[i] = 1 if child[i] == 0 else 0
            return child
            
        popCopy = self.population[:]
        for i in range(len(self.population)):
            parent1 = self.population[i]
            self.population[i] = mutate(crossover(parent1,popCopy))
         
    def develop(self,generation = 200):
        for i in range(generation):
            self.translate()
            self.getFitness()
            if i == 0:
                print("Most fitted DNA: ", self.population[np.argmax(self.fitness)])
            self.select()
            self.mute
            print('Generation {}'.format(i))
            print(self.population)
        
def test():
    jelly = species()
    jelly.develop(10)            
        
        
'''    
def test():
    temp = species()
    temp.translate()
    print(temp.translated)
    temp.getFitness()
    print(temp.fitness)
    temp.select()
    print(temp.population)
    temp.mute()
    print(temp.population)
'''