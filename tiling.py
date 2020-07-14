
def tiling(n):
    if(arr[n] != -1):
        return arr[n] 
    if(n == 1 or n == 2):
        arr[n] = n
        return arr[n]
    arr[n] = tiling(n-1)+tiling(n-2)
    return arr[n]

n = 6
arr = [-1 for i in range(n+1)]
print(tiling(n))
print(arr)