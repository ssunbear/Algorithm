import sys
input=sys.stdin.readline

n=int(input())
dp=[0 for _ in range(31)]
dp[2]=3
for i in range(4,n+1,2):
    dp[i]=3*dp[i-2]+(sum(dp[:i-2])+1)*2

print(dp[n])