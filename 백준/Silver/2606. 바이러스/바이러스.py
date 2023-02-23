import sys
input = sys.stdin.readline
from collections import deque

n=int(input())
m=int(input())
graph=[[] for i in range(n+1)]

for i in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(1,n+1):
    graph[i].sort()

visited=[False]*(n+1)
cnt=0

def bfs():
    queue=deque([1])
    visited[1]=True
    global cnt
    while queue:
        v=queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                cnt+=1
                queue.append(i)
                visited[i]=True

bfs()
print(cnt)