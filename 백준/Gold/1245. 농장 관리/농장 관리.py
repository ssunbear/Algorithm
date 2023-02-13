import sys
input=sys.stdin.readline
from collections import deque

n, m=map(int, input().split())
data=[] 
for i in range(n):
    data.append(list(map(int, input().split())))

dx=[-1,-1,-1,0,0,1,1,1] 
dy=[-1,0,1,1,-1,-1,0,1]

checkidx=[]

def bfs(x, y, checkidx):
    q=deque([(x,y)])
    visited[x][y]=1
    check=[(x, y)]
    while q:
        X, Y= q.popleft()
        for i in range(8):
            nx, ny= X+dx[i], Y+dy[i] 
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if visited[nx][ny]==1:
                continue
            if data[X][Y]<data[nx][ny]:
                return 0
            if data[X][Y]==data[nx][ny]:
                visited[nx][ny]=1
                q.append((nx,ny))
                check.append((nx,ny))
        checkidx+=check 
    return 1

tot=0
for i in range(n):
    for j in range(m):
        if (i, j) not in checkidx:
            visited=[[0]*m for _ in range(n)]
            tot+=bfs(i,j,checkidx)
print(tot)