# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 11:19:09 2018

@author: 11658
"""



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
            
        

    
    
        
    