import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))
dp=[1]*n
dp1=[1]*n 
dp2=[1]*n

for i in range(n):
    for j in range(i):
        if array[i]>array[j]:
            dp1[i]=max(dp1[j]+1, dp1[i])
for i in range(n-1,-1,-1):
    for j in range(n-1, i, -1):
        if array[i]>array[j]:
            dp2[i]=max(dp2[j]+1, dp2[i])

for i in range(n):
    dp[i]=dp1[i]+dp2[i]-1

print(max(dp))