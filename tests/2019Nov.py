import random
def isValidMatrix(n,MAT):
    isValid = True
    for i in range(n):
        for j in range(n):
            if (abs(i-j)<2 and MAT[i][j] == 0) or (abs(i-j)>2 and MAT[i][j] != 0):
                isValid = False
    return isValid

def mystery(A,R):
    return A[R][R-1] + mystery(A,R-1) if R>0 else 0

if __name__ == "__main__":
    M = [[random.randint(0,9) for i in range(6)] for i in range (6)]
    print(M)
    print(isValidMatrix(6,M))
    print(mystery(M,5))