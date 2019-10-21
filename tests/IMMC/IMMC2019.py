import xlrd
import numpy as np
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
data=xlrd.open_workbook("data.xlsx")
table=data.sheets()[0]
data=[]
for i in range(2,103):
    temp = table.row_values(i,2,103)
    data += temp
Y = np.array(data)#.reshape(10201,1)


x = []
for i in range(0,101):
    #x.append([])
    for j in range(0,101):
        x.append([j,i])
X = np.array(x,dtype = float)


#def interSum(Array,p):
#    myArray = np.square(Array-p)
#    temp = np.zeros(len(myArray),dtype = float)
#    for i in range(len(myArray)):
#        temp[i] = myArray[i][0]+myArray[i][1]
#        if temp[i] == 0:
#            temp[i] = 1
#    return temp

def interSum(xx,p):

    t = np.zeros(len(xx),dtype = float)
    s=(xx-p)*1000
    for i in range(len(s)):
        t[i] = (s[i][0]**2+s[i][1]**2)**0.5
    t[t==0]=1000
    return t
'''
def func1(x,Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3):
    p1 = np.array([m1,n1])
    p2 = np.array([m2,n2])
    p3 = np.array([m3,n3])

    def interSum(xx,p):
        t = np.zeros(len(xx),dtype = float)
        s=(xx-p)*1000
        for i in range(len(s)):
            t[i] = (s[i][0]**2+s[i][1]**2)
        t[t==0]=1000
        return t
    return  2*(Q1/(8*(math.pi*k*100)**(3/2))*math.exp(-(interSum(x,p1))/(4*k*100))+ Q2/(8*(math.pi*k*100)**(3/2))*math.exp(-(interSum(x,p2))/(4*k*100))+ Q3/(8*(math.pi*k*100)**(3/2))*math.exp(-(interSum(x,p3))/(4*k*100)))
'''
def func1(x, Q1,Q2,Q3,k):
    p1 = np.array([69,45])
    p2 = np.array([43,61])
    p3 = np.array([35,54])
    return 1*(Q1 / (4*math.pi*k*interSum(x,p1))+ Q2 / (4*math.pi*k*interSum(x,p2)) + Q3 / (4*math.pi*k*interSum(x,p3)))

popt, pcov = curve_fit(func1, X, Y ,bounds = ([0,0,0,0],[10000,10000,10000,10000]), maxfev=100000)




def func(x, Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3):
    p1 = np.array([m1,n1])
    p2 = np.array([m2,n2])
    p3 = np.array([m3,n3])
    return 2*(Q1 / (4*math.pi*k*interSum(x,p1))+ Q2 / (4*math.pi*k*interSum(x,p2)) + Q3 / (4*math.pi*k*interSum(x,p3)))

#popt, pcov = curve_fit(func, X, Y, p0 = [1000,1000,1000,100,69,46,37,56,45,60] ,bounds = ([0,0,0,0,0,0,0,0,0,0],[4000,4000,4000,100,100,100,100,100,100,100]),maxfev=100000)

#popt, pcov = curve_fit(func, X, Y,  p0 = [30,30,30,6000,69,45,43,61,35,54] ,bounds = ([0,0,0,0,0,0,0,0,0,0],[100,100,100,10000,100,100,100,100,100,100]),maxfev=100000)

#popt, pcov = curve_fit(func, X, Y, maxfev=20000)

Q1 = popt[0]
Q2 = popt[1]
Q3 = popt[2]
k = popt[3]
'''
m1 = popt[4]
n1 = popt[5]
m2 = popt[6]
n2 = popt[7]
m3 = popt[8]
n3 = popt[9]
'''
#yvals =  func(X, Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3)
yvals =  func1(X, 1677,1834,1749,0.936133)
#yvals =  func(X, 100,100,100,0.5,5,5,18,18,77,77)
#yvals = func(X, )
yvals1 = yvals.reshape(101,101)
plt.matshow(yvals1, cmap = plt.cm.cool, vmin=0, vmax=1)
plt.colorbar()
plt.show()