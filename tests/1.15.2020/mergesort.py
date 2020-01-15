def mergeSort(x):
    def merge(m,n):
        result = []
        mi = 0
        ni = 0
        while True:
            if mi >= len(m):
                result += n[ni:ni+1]
                return result
            if ni >= len(n):
                result += m[mi:mi+1]
                return result
            if m[mi] <= n[ni]:
                result += m[mi:mi+1]
                mi += 1
            else:
                result += n[ni:ni+1]
                ni += 1
    if len(x) <= 1:
        return x
    mid = int(len(x)/2)
    left = mergeSort(x[:mid])
    right = mergeSort(x[mid:])
    return merge(left,right)

if __name__ == "__main__":    
    print(mergeSort([5,2,3,7,9,1,8,4]))
