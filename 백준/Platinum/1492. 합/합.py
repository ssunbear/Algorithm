def factor(n): # 이항계수 계산용 팩토리얼
    result = 1
    for i in range(2,n+1):
        result *= i
    return result

def square(a,n):
    if n == 1:
        return a
    x = square(a,n//2)
    if n % 2 == 0 :
        return x*x % mod
    else : 
        return x*x*a %mod

def combin(n,k): # 조합 갯수 결과 (페르마의 소정리)
    a = factor(n) % mod
    b = square(factor(k) * factor(n-k), mod-2) % mod
    return a*b % mod

import sys
N, p = map(int,sys.stdin.readline().split())
mod = 10**9+7
dp = [0] * (p + 1)
dp[0] = N
for i in range(1, p+1):
    t = 0
    x = (N+1) **(i+1) - 1 # 제곱의 합 구하는 공식
    for j in range(i):
        t += combin(i+1,j) * dp[j] # 이항계수 (i+1, j) * 이전 공식 사용한 것들의 합
    y = combin(i+1,i) # 각 계수
    # 다음 dp는 x-y를 (i+1,i)의 이항계수로 나눈 값
    dp[i] = (((x-t) % mod) * (square(y,mod-2) % mod)) % mod #(제곱의 합- 계수 합) * 이항 계수의 역수(페르마의 소정리)
print(dp[p] % mod)