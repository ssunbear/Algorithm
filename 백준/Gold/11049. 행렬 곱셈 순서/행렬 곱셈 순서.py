n = int(input())
arr = []
dp = [[0]*n for _ in range(n)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1,n):              
    for j in range(n-i):        
        x = i + j
        dp[j][x] = 2 ** 31
        for k in range(j,x):   
            dp[j][x] = min(dp[j][x], dp[j][k] + dp[k+1][x] + arr[j][0] * arr[k][1] * arr[x][1])

print(dp[0][n-1])