
def friend(n):
    if(n <= 2):
        return n
    return friend(n-1) + (n-1)*friend(n-2)    

def friendDp(n):
    if(dp[n] != -1):
        return dp[n]
    if(n <= 2 ):
        dp[n] = n
        return dp[n]
    dp[n] = friendDp(n-1)+(n-1)*friendDp(n-2)
    return dp[n]        


n = 4
dp = [-1] *(n+1)
print(friendDp(n))
print(dp)