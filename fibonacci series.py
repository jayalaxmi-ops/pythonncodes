#def fibo(n,dp):
    #if(n==0):
        #return 0    # T.C :-O(N)  S.C:-O(N)+O(N)
    #if(n==1):
        #return 1
    #if(dp[n]!= -1):
        #return dp[n]
    #dp[n]=fibo(n-1,dp)+fibo(n-2,dp)
    #return dp[n]
#n=int(input())
#dp=[-1]*(n+1)
#print(fibo(n,dp))





def fibo(n,dp):
    dp[0]=0
    dp[1]=1
    for ind in range(2,n+1): # t.C:-O(N)
        dp[ind]=dp[ind-1]+dp[ind-2]
    return dp[n]
n=int(input())
dp=[-1]*(n+1)  #S.C:-O(N)
print(fibo(n,dp))
 
