# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 12:49:52 2018

@author: 11658
"""

import matplotlib.pyplot as plt
import numpy as np

class deliveryRoute():
   
    def __init__(self,cityPosition,popSize = 500,crossRate = 0.6,mutateRate = 0.05):
        '''
        Must give the position of the places in array e.g.[0.1,0.2],[0.3,0.4],[0.5,0.6]
        popSize = 500
        crossRate = 0.1
        mutateRate = 0.02
        '''

        self.cityPosition = cityPosition
        self.DNALength = len(self.cityPosition)
        self.popSize = popSize   
        self.crossRate = crossRate
        self.mutateRate = mutateRate
        
        
        self.population = np.vstack([np.random.permutation(self.DNALength) for i in range(self.popSize)])
        self.bestFitness = 0
        self.countDown = 500
        
  
    def translate(self):
        '''
        tranlate the DNA of a route(in the order) into number array
        '''
        for i, j in enumerate(self.population):
            cityCoor = self.cityPosition[j]
            self.xCoor[i, :] = cityCoor[:, 0]
            self.yCoor[i, :] = cityCoor[:, 1]
        
    def getFitness(self):
        '''
        calculate the fitness of each route
        '''
        for i, (x, y) in enumerate(zip(self.xCoor, self.yCoor)):
            self.totalDistance[i] = np.sum(np.sqrt(np.square(np.diff(x)) + np.square(np.diff(y))))#某公式计算每一种DNA下所有路程的总距离
        self.fitness = np.exp(self.DNALength * 2 / self.totalDistance)

    def select(self):
        '''
        select survive route according to fitness
        '''
        index = np.random.choice(a = np.arange(self.popSize),size = self.popSize,replace  = True,p = self.fitness / sum(self.fitness))
        self.population = self.population[index]
    
    
    def mute(self): #Uniform crossover
        '''
        the process of crossover and mutate
        '''
        
        def crossover( parent1, popCopy):
            if np.random.rand() < self.crossRate:
                temp = np.random.randint(low = 0,high = self.popSize,size = 1)                       # select another individual from pop
                crossPoints = (np.random.randint(low = 0,high =  2, size = self.DNALength)).astype(np.bool)   # choose crossover points
                keep = parent1[crossPoints]                                       # find the city number
                change = popCopy[temp, np.isin(popCopy[temp].ravel(), keep, invert=True)]
                parent1[:] = np.concatenate((keep, change))
            return parent1
        

        
        def mutate(child):
            for point in range(self.DNALength):
                if np.random.rand() < self.mutateRate:
                    mutatePoint = np.random.randint(low = 0, high =self.DNALength)
                    child[point], child[mutatePoint] =  child[mutatePoint],child[point]
            return child
        popCopy = self.population[:]
        for i in range(len(self.population)):
            parent1 = self.population[i]
            self.population[i] = mutate(crossover(parent1, popCopy))
            
    def plotting(self):
        plt.cla()
        plt.scatter(self.cityPosition[:, 0].T, self.cityPosition[:, 1].T, s=100, c='k')
        plt.plot(self.xCoor[self.bestIndex].T, self.yCoor[self.bestIndex].T, 'r-')
        plt.text(-0.05, -0.05, "Total distance%.2f" % self.totalDistance[self.bestIndex], fontdict={'size': 20, 'color': 'red'})
        #plt.xlim((-0.1, 1.1))
        #plt.ylim((-0.1, 1.1))
        plt.pause(0.01)
        

    def develop(self,generation = 500):
        '''
        develop the routes for generation times
        generation default value is 200
        '''
        for i in range(generation):
            
            #if countDown == 0:-----------
                #self.disaster()-----------
                
            self.translate()
            self.getFitness()
            self.select()
            self.mute()   
            self.bestIndex = np.argmax(self.fitness)
            if max(self.fitness) > self.bestFitness:
                self.bestFitness = max(self.fitness)
                self.bestX = self.xCoor[self.bestIndex]
                self.bestY = self.yCoor[self.bestIndex]
                self.bestDistance = self.totalDistance[self.bestIndex]
                self.bestDNA = self.population[self.bestIndex]
                self.countDown = (500-self.countDown)*2.5
            else:
                self.countDown -= 1
            
            print('Generation {}'.format(i))
            
            self.plotting()
        plt.ioff()
        plt.show()
        
        return(self.cityPosition[self.bestDNA])


def test(n):
    '''
    n 为城市数
    因未加入精英策略优化
    算法可能丢掉最优解
    我用self.bestDistance 和 self.bestDNA 记录了最优解
    '''
    temp = (np.random.rand(n, 2))
    
    jelly = deliveryRoute(temp)      
    jelly.develop(200)
    return(temp)
    
if __name__ == '__main__':
    test(18)
