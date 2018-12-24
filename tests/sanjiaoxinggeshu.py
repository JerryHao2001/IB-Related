# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 16:09:54 2018

@author: 11658
"""
'''
n = int(input('length?'))
solution = []
count = 0
for i in range(1,n-1):
    for j in range(1,n-1):
        k = n - i - j
        judge = True
           
        if not((i+j)>k and (i+k)>j and (j+k)>i):
            judge = False

        for s in solution:
            if (i in s) and (j in s) and (k in s):
                judge = False

        if judge:         
            solution.append([i,j,k])
            count += 1
    
print(count)
'''
n=int (input("please input the length of the rob:"))	
cnt=0											
for i in range(n):									
    for j in range(n-i):
        k=n-i-j
        if i<=j<=k and i+j>k and j+k>i and i+k>j:			
            cnt+=1
            print(i,j,k)
print(cnt)					
