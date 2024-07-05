N, p = map(int, input().split())
mod = 10**9+7
C = [[1]*(p+2) for _ in range(p+2)]
for i in range(1,p+2): # 파스칼의 삼각형을 이용한 이항계수
   for j in range(1,i):
      C[i][j] = C[i-1][j-1] + C[i-1][j]
dp = [0]*(p+1)
dp[0] = N

for i in range(1,p+1):
   x = (N+1)**(i+1) -1 # 누적 합 공식
   for j in range(i): # 누적합에서 이전 꺼 차이를
      x -= C[i+1][j] * dp[j] 
   dp[i] = x // (i+1) # 이항계수로 나눠주기

print(dp[p] % mod) # 결과