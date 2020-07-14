def coinChange(coin,sum,n):
    if(sum == 0):
        return 1
    if( n <= 0):
        return 0
    if(coin[n-1] <= sum):
        return coinChange(coin,sum,n-1) + coinChange(coin,sum-coin[n-1],n)
    else:    
        return coinChange(coin,sum,n-1)

def cointDp(coin,sum,n):
    if(dp[n][sum] != -1):
        return dp[n][sum]
    if(sum == 0):
        dp[n][sum] = 1
        return dp[n][sum]
    if(n == 0):
        dp[n][sum] = 0
        return dp[n][sum]

    if(coin[n-1] <= sum):
        dp[n][sum] = cointDp(coin,sum,n-1) + cointDp(coin,sum-coin[n-1],n)
        return dp[n][sum]
    else:
        dp[n][sum] = cointDp(coin,sum,n-1)
        return dp[n][sum]               

def space(coin,sum,n):
    dp = [0 for i in range(sum+1)]
    dp[0] = 1
    for i in range(0,n):
        for j in range(coin[i],sum+1):
            dp[j] += dp[j-coin[i]]
    return dp[sum]        

arr = [1,2,3]
n = len(arr)
sum = 5
# dp = [[-1 for i in range(sum+1)] for j in range(n+1)]
# for i in range(1,sum+1):
    # dp[0][i] = 0
# for j in range(n+1):
    # dp[j][0] = 1    
print(space(arr,sum,n))   
# print(dp)             
