import random

def selectSort(x):
    for i in range(len(x)-1):
        min = i
        for j in range(i,len(x)):
            if x[j]<x[min]: min = j
        if min!=i: x[i],x[min] = x[min],x[i]
    return x

def bubbleSort(x):
    for i in range(len(x)-1):
        if x[i] > x[i+1]: x[i],x[i+1]=x[i+1],x[i]
    return x[:1] + bubbleSort(x[1:]) if len(x)>1 else x[:1]


if __name__ == "__main__":
    VALUES = [random.randint(0,100) for i in range (8)]
    print(VALUES)
    print(selectSort(VALUES))
    print(bubbleSort(VALUES))