import math

check = [False] * 4000001
Prime = [0] * 4000001

def eratosthenes(N):
    for i in range(2, int(math.sqrt(N)) + 1):
        if not check[i]:
            for j in range(i + i, N + 1, i):
                check[j] = True

def calculate(N, K):
    for i in range(2, N + 1):
        if not check[i]:
            factor = i
            while factor <= N:
                Prime[i] += (N // factor) - (K // factor) - ((N - K) // factor)
                factor *= i


N, K, M = map(int, input().split())
eratosthenes(N)
calculate(N, K)

ans = 1
for i in range(2, N + 1):
    for _ in range(Prime[i]):
        ans = (ans*i)%M
print(ans)