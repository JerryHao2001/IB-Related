# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import time

def cubeRoot(n):
    for ans in range(0, abs(n)+1):
        if ans**3 >= abs(n):
                break
    if ans**3 != abs(n):
        print(n, 'is not a perfect cube')
    else:
        if n < 0:
            ans = -ans
        print ('Cube root of', n,'is', ans)

def cubeRoot1(n):
    n = int(input('Enter an integer: '))
    ans = 0
    while ans**3 < abs(n):
        pass
    if ans**3 != abs(n):
        print (n, 'is not a perfect cube')
    else:
        if n < 0:
            ans = -ans
    print ('Cube root of', n,'is', ans)
    
def summ(n):
    start = time.time()
    temp = 0
    for i in range(1,n+1):
        temp += i
    end = time.time()
    return temp,end-start
        
def digitSum(s):
    temp = 0
    for i in s:
        if i.isdigit():
            temp += int(i)
    return(temp)
            
def squareRoot(x):
    epsilon = 0.001
    step = epsilon**2
    numGuesses = 0
    ans = 0.0
    while abs(ans**2 - x) >= epsilon and (ans <= x or ans*ans <= x):
        ans += step
        numGuesses += 1
    print ('numGuesses =', numGuesses)
    if abs(ans**2 - x) >= epsilon:
        print ('Failed on square root of', x)
    else:
        print (ans, 'is close to square root of', x)

def squareRootI(x):
    epsilon = 0.01
    guess = 0
    low = min(0,x)
    high = max(1,x)
    ans = (high + low) / 2
    while abs(ans**2 -x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        guess += 1
        if ans ** 2 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print ('numGuesses =', guess)
    print (ans, 'is close to square root of', x)

def cubeRootII(x):
    epsilon = 0.001
    guess = 0
    low = 0
    high = max(1,abs(x))
    ans = (high + low) / 2
    while abs(ans**3-abs(x)) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        guess += 1
        if ans ** 3 < abs(x):
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    print('numGuesses =', guess)
    if x < 0:
        ans = -ans
    print (ans, 'is close to square root of', x)
        
class uFather():
    def __init__(self,temp,temp1,temp2):
        self.temp = temp
        self.temp1 = temp1
        self.temp2 = temp2
    def check(self,n):
        print(self.temp,self.temp1,self.temp2)
        print(n)

