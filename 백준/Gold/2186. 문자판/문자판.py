dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def dfs(x, y, idx):
    if idx >= len(target):  
        return 1            
    if dp[x][y][idx] != -1:
        return dp[x][y][idx]  

    dp[x][y][idx] = 0  
    for i in range(4):
        tmp_x, tmp_y = x, y
        # k는 이동 한도 범위를 나타냄
        for _ in range(k):
            nx = tmp_x + dx[i]
            ny = tmp_y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == target[idx]:
                    dp[x][y][idx] += dfs(nx, ny, idx + 1)
            tmp_x, tmp_y = nx, ny  # k가 2 이상일 때 사용하기 위해
    return dp[x][y][idx]


n, m, k = map(int, input().split())


matrix = []
for _ in range(n):
    matrix.append(list(input()))

target = list(input())
start = []

for i in range(n):
    for j in range(m):
        if matrix[i][j] == target[0]:
            start.append([i, j])

dp = [[[-1] * len(target) for _ in range(m)] for _ in range(n)]
res = 0
for i in range(len(start)):
    x, y = start[i]
    res += dfs(x, y, 1)
print(res)