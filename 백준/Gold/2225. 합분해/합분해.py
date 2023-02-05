import sys
input=sys.stdin.readline

n, k=map(int, input().split())
mod=1000000000
dp=[1 for i in range(n+1)]
for i in range(2,k+1):
    for j in range(1,n+1):
        dp[j]=(dp[j]+dp[j-1])%mod
        
print(dp[n])