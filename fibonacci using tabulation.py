def fibo(n,dp):
    dp[0]=0
    dp[1]=1
    for ind in range(2,n+1):
        dp[ind]=fibo(ind-1,dp)+fibo(ind-2,dp)
    return dp[n]
n=int(input())
dp=[-1]*(n+1)
print(fibo(n,dp))
