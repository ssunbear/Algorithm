import sys
input=sys.stdin.readline
from collections import deque

n, m=map(int, input().split())
data=[list(map(int, input().split())) for _ in range(n)]

visted=[[False for i in range(m)] for j in range(n)]
dx=[-1,-1,-1,0,0,1,1,1]
dy=[-1,0,1,-1,1,-1,0,1]

def bfs(x,y):
    visited=[[False for i in range(m)] for j in range(n)]
    dx=[-1,-1,-1,0,0,1,1,1]
    dy=[-1,0,1,-1,1,-1,0,1]
    visited[x][y]=True
    q=deque([(x,y,0)])

    while q:
        x, y, dis= q.popleft()
        for i in range(8):
            nx, ny= x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if data[nx][ny]==0:
                    q.append((nx,ny,dis+1))
                    visited[nx][ny]=True
                else:
                    return dis+1

res=0
for i in range(n):
    for j in range(m):
        if data[i][j]==0: 
            res=max(res, bfs(i,j))

print(res)
