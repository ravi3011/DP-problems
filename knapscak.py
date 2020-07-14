
def knapSack(wait,wt,val,n):
    if( n is 0 or wait is 0):
        return 0
    if(dp[n][wait] != -1):
        return dp[n][wait]

    if(wt[n-1] <= wait):
        dp[n][wait] = max(val[n-1]+knapSack(wait-wt[n-1],wt,val,n-1),knapSack(wait,wt,val,n-1))
        return dp[n][wait]
    elif(wt[n-1] > wait):
        dp[n][wait] = knapSack(wait,wt,val,n-1)    
        return dp[n][wait]

def itrKnapSack(wt,val,w,n):
    dp = [[0 for x in range(w+1)] for x in range(n+1)]

    for i in range(n+1):
        for j in range(w+1):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif(wt[i-1] <= j):
                dp[i][j] = max(val[i-1]+dp[i-1][j-wt[i-1]],dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[n][w]                    


if(__name__=="__main__"):
    val = [60,100,120]
    wt = [10,20,30]
    wait = 50
    # dp = [[-1 for i in range(wait+1)] for i in range(len(val)+1)]
    print(itrKnapSack(wt,val,wait,len(val)))    