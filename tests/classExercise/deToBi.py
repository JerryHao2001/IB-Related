# -*- coding: utf-8 -*-
"""
Created on Thu Sep 13 10:59:54 2018

@author: 11658
"""

def deToBi(n):
    result = ''
    isNeg = False
    if n < 0:
        isNeg = True
        n = abs(n)
    elif n == 0:
        return 0    
    while n >= 1:
            result = str(n%2) + result
            n = n//2
    if isNeg:
        return '-'+result
    return result

    
def deToHex(n):
    temp = {"10" : 'A',"11" : 'B',"12" : 'C','13' : 'D','14' : 'E','15' : 'F'}
    result = ''
    isNeg = False
    if n < 0:
        isNeg = True
        n = abs(n)
    elif n == 0:
        return 0
    while n >= 1:
        if n % 16 > 9:
            result = temp[str(n % 16)] + result
        else:
            result = str(n % 16) + result
        n = n//16
    if isNeg:
        return '-'+result
    return result

# 小数转换
def deToBiI(x):
    p = 0
    while ((2**p)*x)%1 != 0:
        print('Remainder = ' + str((2**p)*x - int((2**p)*x)))
        p += 1
    num = int(x*(2**p))
    result = ''
    if num == 0:
        result = '0'
    while num > 0:
        result = str(num%2) + result
        num = num//2
    for i in range(p - len(result)):
        result = '0' + result
    result = result[0:-p] + '.' + result[-p:]
    return('The binary representation of the decimal ' + str(x) + ' is' + str(result))
    
def squareRootNewton(x):
    epsilon = 0.01
    guess = x/2
    while abs(guess*guess - x)>= epsilon:
        guess = guess - ((guess**2-x)/(2*guess))
    return ('Square root of', x,'is about', guess)
    