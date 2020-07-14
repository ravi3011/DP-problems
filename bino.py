def bino(n,k):
    if(k==0 or n==k):
        return 1
    else:
        return bino(n-1,k-1) + bino(n-1,k)

def binoM(n,k):
    if(arr[n][k] != -1):
        return arr[n][k]

    if(k==0 or n==k):
        arr[n][k] = 1
        return arr[n][k]
    
    arr[n][k] = binoM(n-1,k-1) + binoM(n-1,k)
    return arr[n][k]


def binoDp(n,k):
    dp = [[0 for i in range(k+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(min(i,k)+1):
            if(j == 0 or j == i):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
    return dp[n][k]                


if(__name__=='__main__'):
    arr = [[-1 for i in range(3)] for j in range(6)]
    print(binoM(5,2))