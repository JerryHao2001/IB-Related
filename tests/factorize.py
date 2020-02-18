# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 23:41:34 2018

@author: 11658
"""
import time
import random

'''
from math import log
def factorize(n):
    result = []
    m = n
    for i in range(int(log(m,2))+1):
        temp = 2
        for j in range(temp,min([int(m**0.5),int(n+1)])):            
            if n%j == 0:
                result.append(str(j))
                temp = j
                n = n//j
                break
        
    result = '*'.join(result)
    return(result)
'''

def fact(n):
    factor = -1
    min = 2
    for i in range(min,int(n**0.5)):
        if n%i == 0:
            factor = i
            min = i
            break
        else:
            continue
    if  factor == -1:
        print(f'{n}(prime)')
        return ''
    print(f"{factor}*", end='')
    return fact(n//factor)

if __name__ == '__main__':
    time_test = []
    for i in range(3):
        test = random.randint(10000000000000000000,99999999999999999999) #20
        print(f"test number: {test}")
        start_time = time.time()
        print(f"{fact(test)}")
        end_time = time.time()
        time_test.append(end_time-start_time)
    print(time_test)
    print(sum(time_test)/len(time_test))

            