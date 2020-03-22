def fill(n):
    z = 1
    top,bottom,left,right = 0,n-1,0,n-1
    a = [[i for i in range(0,n)] for i in range(0,n)]
    while z <= n**2:
        for i in range(left,right+1):
            a[top][i] = z
            z += 1
        top+=1
        for i in range(top,bottom+1):
            a[i][right] = z
            z += 1
        right-=1
        for i in range(right,left-1,-1):
            a[bottom][i] = z
            z+=1
        bottom -=1
        for i in range(bottom,top-1,-1):
            a[i][left] = z
            z+=1
        left+=1
    return a

if __name__ == "__main__":
    array = fill(5)
    for i in array:
        print(i,end="\n")
