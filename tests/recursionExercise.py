# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 08:05:21 2018

@author: 11658
"""
import turtle


def sum_recur(n):
    '''inpur:n(int)
    output:1+2+3...+n'''
    if n == 1:
        return 1
    else:
        return n + sum_recur(n-1)

def fac_recur(n):
    '''input:n(int)
    output:n!'''
    if n == 1:
        return 1
    else:
        return n * fac_recur(n-1)
def power_recur(a,b):
    '''input:a,b(int,b>0)
    output:a^b'''
    if b == 0:
        return 1
    else:
        return a * power_recur(a,b-1)


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)        
def fib_sum(n):
    if n == 0:
        return 1
    else:
        return fib(n) + fib_sum(n-1)


t = turtle.Turtle()

def fractal(n = (-300.00,-200.00),l = 270):
    t.speed(100)
    t.color('blue')
    if l > 5:
        t.up()
        t.goto(n)
        t.down()
        t.fd(l)
        b = t.pos()
        t.lt(120)
        t.fd(l)
        c = t.pos()
        t.lt(120)
        t.fd(l)
        t.lt(120)
        jelly(b,l/2)
        jelly(c,l/2)
        
     
print(sum_recur(4))
print(fac_recur(4))
print(power_recur(3,2))
print(fib(5),fib_sum(5))
fractal()
