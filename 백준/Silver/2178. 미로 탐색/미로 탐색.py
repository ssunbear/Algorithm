import sys
input = sys.stdin.readline
from collections import deque

n,m=map(int, input().split())
graph=[list(map(int, input().strip())) for _ in range(n)]
visited=[[False for i in range(m)] for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(x,y):
    queue=deque()
    queue.append([x,y])
    while queue:
        x, y= queue.popleft()
        if x==n-1 and y==m-1:
            print(graph[n-1][m-1])
            return
        for i in range(4):
            nx, ny= x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny]==1 and not visited[nx][ny]:
                    graph[nx][ny]=graph[x][y]+1
                    visited[nx][ny]=True
                    queue.append([nx,ny])

bfs(0,0)