N = int(input())
price=[]
for i in range(N):
    price.append([int(x) for x in input()])

DP = [[[0] * 10 for _ in range(N)] for _  in range(1 << N)]

def dfs(v, s, p):
    if DP[v][s][p] != 0:
        return DP[v][s][p]
    
    cnt = 0
    for i in range(N):
        if v & 1 << i <= 0: # visit에서는 i가 아직 그림X
            if p <= price[s][i]: # 가격 p에 s가 i한테 그림 판매O
                cnt = max(cnt, dfs(v | 1 <<i, i, price[s][i]) + 1)

    DP[v][s][p] = cnt

    return cnt

print(1 + dfs(1, 0, 0))