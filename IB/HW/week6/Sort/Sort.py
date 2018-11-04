# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 10:58:56 2018

@author: 11658
"""

def selectSort(n):
    '''
    input: list x
    outpur: sorted list x
    '''
    for i in range(len(n)):
        least = i
        for j in range(i,len(n)):
            if n[least] > n[j]:
                least = j
        temp = n[i]
        n[i] = n[least]
        n[least] = temp
    return n

def bubbleSort(n):
    """
    input: list n
    output: sorted list n
    """
    for i in range(len(n)-1):
        for j in range(len(n)-1):
            if n[j] > n[j+1]:
                temp = n[j]
                n[j] = n[j+1]
                n[j+1] = temp
    return(n)

def insertSort(n):
    '''
    input: list x
    outpur: sorted list x
    '''

    result = [n[0]]
    for i in range(1,len(n)):
        result += [n[i]]
        for i in range(1,len(result)):
            if result[-i] < result[-i-1]:
                temp = result[-i]
                result[-i] = result[-i-1]
                result[-i-1] = temp
    return result
        

def mergeSort(x):
    '''
    input: list x
    outpur: sorted list x
    '''
    def merge(m,n):
        result = []
        mi = 0
        ni = 0
        while True:
            if mi >= len(m):
                #result.extend(n[ni:])
                result += n[ni:ni+1]
                return result
            if ni >= len(n):
                #result.extend(m[mi:])
                result += m[mi:mi+1]
                return result
            if m[mi] <= n[ni]:
                #result.append(m[mi])
                result += m[mi:mi+1]
                mi += 1
            else:
                #result.append(n[ni])
                result += n[ni:ni+1]
                ni += 1
    if len(x) <=1 :
        return x
    mid = int(len(x) / 2)
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])
    return merge(left,right)


def quickSort(array,left,right):    
    '''
    array: the array u wanna sort
    left: start at left
    right: end at right
    '''    
    def sort(array,left,right):
        '''
        sort once
        '''
        split = array[left]
        while left < right:
            while left < right and array[right] >= split:
                right -= 1
            while left < right and array[right] < split:
                array[left] = array[right]
                left += 1
                array[right] = array[left]
            array[left] = split
        return left

    if left < right:
        split = sort(array,left,right)
        quickSort(array,left,split)
        quickSort(array,split+1,right)
    return array
def useQuickSort(array):
    quickSort(array,0,len(array)-1)

            
def speedTest(n):
    '''
    input: sort function
    test the speed of one sort
    output: list of time
    '''
    from time import clock
    from random import shuffle
    timeList = []
    lengthList = [i for i in range(1000,6000,1000)]
    for i in lengthList:
        temp = [j for j in range(i,0,-1)]
        shuffle(temp)
        start = clock()
        n(temp)
        end = clock()
        timeList.append(end-start)
    return timeList

def illustrate():
    '''
    illustrate the speed in graph
    '''
    import matplotlib.pyplot as plt
    func = [selectSort,bubbleSort,insertSort,mergeSort,useQuickSort]
    funcName = ['selectSort','bubbleSort','insertSort','mergeSort','quickSort']
    for i in range(5):
        plt.plot([i for i in range(1000,6000,1000)],speedTest(func[i]), label = funcName[i])
    plt.xlabel('length of step list')
    plt.ylabel('running time(s)')
    plt.legend()
    plt.show()
        


