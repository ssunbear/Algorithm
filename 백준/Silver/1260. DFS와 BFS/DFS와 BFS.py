import sys
from collections import deque
input = sys.stdin.readline

n,m,v=map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

dfsvisited=[False]*(n+1)
bfsvisited=[False]*(n+1)

def dfs(graph, u, dfsvisited):
    dfsvisited[u]=True
    print(u, end=' ')
    for i in graph[u]:
        if not dfsvisited[i]:
            dfs(graph,i,dfsvisited)

def bfs(graph, u, bfsvisited):
    queue=deque([u])
    bfsvisited[u]=True
    while queue:
        v1=queue.popleft()
        print(v1, end=' ')
        for i in graph[v1]:
            if not bfsvisited[i]:
                queue.append(i)
                bfsvisited[i]=True

dfs(graph,v,dfsvisited)
print()
bfs(graph, v, bfsvisited)