L1 = {"Pizarra":4,"Alora":3,"Alamo":3,"Lomas":2,"Torrox":1,"Centro":0}
L2 = {"Fuengirola":4,"Prados":4,"Lima":3,"Plaza Mayer":3,"David":2,"Col":1,"Centro":0}
S = sorted(list(set([i for i in L1.keys()]+[i for i in L2.keys()])))
def getZone(station):
    return L1[station] if station in L1 else L2[station]

def getLine(station):
    return 1 if station in L1 else 2

def getFare(L1,L2,S):
    table = [[[]for i in range(len(S))] for i in range(len(S))]
    for i in range(len(S)):
        table[i][i] = 0
        for j in range(i+1,len(S)):
            table[i][j] = table[j][i] = abs(getZone(S[i])-getZone(S[j]))+1 if getLine(S[i])==getLine(S[j]) else getZone(S[i])+getZone(S[j])+1
    return table

if __name__ == "__main__":
    print(getFare(L1,L2,S))
