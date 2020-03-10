import random
def swapRows(MAT,K,L):
    MAT[K],MAT[L]=MAT[L],MAT[K]

def sort(x,y,z):
    for i in range(len(z)-1):
        min = i
        for j in range(i,len(x)):
            if x[j]<x[min]: min = j
        if min!=i:
            swapRows(z,min,i)
            swapRows(y,min,i)
            swapRows(x,min,i)
    return x,y,z


if __name__ == "__main__":
    PLAYERS = ['jerry','helen','charlie']
    ROUNDS = [[random.randint(0,100) for i in range(4)] for i in range (3)]
    TOTALS = [random.randint(0,400) for i in range(3)]
    print(PLAYERS,ROUNDS,TOTALS)
    x,y,z = sort(PLAYERS,ROUNDS,TOTALS)
    print(x,y,z)

    
