import xlrd
import numpy as np
import math
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data=xlrd.open_workbook("data.xlsx")
table=data.sheets()[0]
data=[]
for i in range(41,76):
    temp = table.row_values(i,24,79)
    data += temp
Y = np.array(data)#.reshape(10201,1)


x = []
for i in range(39,74):
    #x.append([])
    for j in range(22,77):
        x.append([j,i])
X = np.array(x,dtype = float)

x1 = []
for i in range(0,101):
    #x.append([])
    for j in range(0,101):
        x1.append([j,i])
X1 = np.array(x1,dtype = float)

#def interSum(Array,p):
#    myArray = np.square(Array-p)
#    temp = np.zeros(len(myArray),dtype = float)
#    for i in range(len(myArray)):
#        temp[i] = myArray[i][0]+myArray[i][1]
#        if temp[i] == 0:
#            temp[i] = 1
#    return temp

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

def func1(x, Q1,Q2,Q3,k):
    p1 = np.array([69,45])
    p2 = np.array([43,61])
    p3 = np.array([35,54])
    return 2*(Q1 / (4*math.pi*k*interSum(x,p1))+ Q2 / (4*math.pi*k*interSum(x,p2)) + Q3 / (4*math.pi*k*interSum(x,p3)))

popt, pcov = curve_fit(func1, X, Y ,bounds = ([0,0,0,0],[10000,10000,10000,10000]), maxfev=100000)
'''

def interSum(xx,p,kk,qq):

    t = np.zeros(len(xx),dtype = float)
    s=(xx-p)*1000
    for i in range(len(s)):
        t[i] = (s[i][0]**2+s[i][1]**2)**0.5
    t[t==0]=qq/(2*math.pi*kk)
    return t


def func(x, Q1,Q2,Q3,k):#,m1,n1,m2,n2,m3,n3):
   p1 = np.array([m1,n1])
   p2 = np.array([m2,n2])
   p3 = np.array([m3,n3])
#  p1 = np.array([69,45])
#  p2 = np.array([43,61])
#  p3 = np.array([35,54])
    return 1*(Q1 / (4*math.pi*k*interSum(x,p1,k,Q1))+ Q2 / (4*math.pi*k*interSum(x,p2,k,Q2)) + Q3 / (4*math.pi*k*interSum(x,p3,k,Q3)))

#popt, pcov = curve_fit(func, X, Y, p0 = [0.4,0.8,0.6,0.02,40,46,37,56,45,60] ,bounds = ([0,0,0,0,0,0,0,0,0,0],[1,1,1,10,100,100,100,100,100,100]),maxfev=100000)

popt, pcov = curve_fit(func, X, Y, p0 = [1000,1000,1000,0.00001] ,ftol = 
                       10**-9)

#popt, pcov = curve_fit(func, X, Y, p0 = [1000,1000,1000,100,69,46,37,56,45,60] ,bounds = ([0,0,0,0,0,0,0,0,0,0],[4000,4000,4000,100,100,100,100,100,100,100]),maxfev=100000)

#popt, pcov = curve_fit(func, X, Y, p0 = [1000,1000,1000,10,69,46,37,56,45,60] ,maxfev=100000 ,ftol = 10**-10)

#popt, pcov = curve_fit(func, X, Y, maxfev=20000)

Q1 = popt[0]
Q2 = popt[1]
Q3 = popt[2]
k = popt[3]

m1 = popt[4]
n1 = popt[5]
m2 = popt[6]
n2 = popt[7]
m3 = popt[8]
n3 = popt[9]

#yvals =  func(X, Q1,Q2,Q3,k,m1,n1,m2,n2,m3,n3)
yvals =  func(X, Q1,Q2,Q3,k)
#yvals =  func(X, 100000000,300000000,12000000,11000000,69,46,37,56,45,60)
yvals1 = func(X1,0.4,0.4,0.4,0.04)
#yvals = yvals.reshape(35,55)
yvals1 = Y.reshape(101,101)
plt.matshow(yvals1, cmap = plt.cm.cool, vmin=0.005, vmax=1.1)
plt.colorbar()
plt.show()
