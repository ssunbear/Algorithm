n,m,k=map(int,input().split())
dp=[[1 for _ in range(m+1)] for _ in range(n+1)]

answer=[]
for i in range(1,n+1):
    for j in range(1,m+1):
        dp[i][j]=dp[i-1][j]+dp[i][j-1]

if dp[n][m]<k:
    print(-1)

else:
    while True:
        if n==0 or m==0:
            answer+=('a'*n+'z'*m)
            break

        s=dp[n-1][m]

        if k<=s:
            answer+='a'
            n-=1
        else:
            k-=s
            answer+='z'
            m-=1


    print(''.join(answer))