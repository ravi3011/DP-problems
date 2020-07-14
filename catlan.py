
def solve(num):
    if(num == 0 or num == 1):
        return 1

    arr = [0 for i in range(num + 1)]

    arr[0] = 1
    arr[1] = 1

    for i in range(2,num + 1):
        arr[i] = 0
        for j in range(i):
            arr[i] = arr[i] + arr[j] * arr[i-j-1]

    return arr[num]            

if(__name__=='__main__'):
    for i in range(10):
        print(solve(i),end=" ")
    print()    