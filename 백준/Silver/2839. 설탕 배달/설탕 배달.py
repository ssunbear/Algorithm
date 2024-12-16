N=int(input())

dp=[-1]*(5001)
dp[3],dp[5]=1,1

if N>5:
    for i in range(5, N+1):
        if dp[i-3]!= -1 and dp[i-5]!=-1:
            dp[i]=min(dp[i-3],dp[i-5])+1
        elif dp[i-3]==-1 and dp[i-5]!=-1:
            dp[i]=dp[i-5]+1
        elif dp[i-3]!=-1 and dp[i-5]==-1:
            dp[i]=dp[i-3]+1

print(dp[N]) 