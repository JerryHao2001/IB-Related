def move(n,a,b,c):
    global count
    '''
    input:n,a,b,c
        n: number of pie move from a though b to c
    output:
        steps
    '''
    if n == 1:
        print(a, '--->', c)
        count += 1
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
def testTower(n):
    global count
    count = 0
    move(n,'a','b','c')
    print(count)
    
