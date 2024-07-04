from collections import *

def BFS():
  dq = deque([0]); parent = [-1]*K
  while dq:
    now = dq.popleft()
    for next in adj[now]:
      if parent[next]<0 and graph[now][next]-flow[now][next]:
        parent[next] = now
        dq.append(next)
        if next==K-1:
          return parent

def update(i,j):
  dq = deque([i]); parent = [-1]*K
  while dq:
    now = dq.popleft()
    for next in adj[now]:
      if 0<next<i or now==i and next<=j or parent[next]!=-1:
        continue
      if graph[now][next]-flow[now][next]:
        parent[next] = now
        dq.append(next)
        if next==j:
          return parent

[N,M],row,column = [[*map(int,input().split())] for i in range(3)]; K = N+M+2
graph,flow = [[[0]*K for i in range(K)] for i in range(2)]
adj = [[] for i in range(K)]
for i in range(1,N+1):
  graph[0][i] = row[i-1]
  adj[0].append(i); adj[i].append(0)
  for j in range(1,M+1):
    graph[i][j+N] = 1
    adj[i].append(j+N); adj[j+N].append(i)
for j in range(1,M+1):
  graph[j+N][K-1] = column[j-1]
  adj[j+N].append(K-1); adj[K-1].append(j+N)
while parent:=BFS():
  now = K-1
  while now:
    last = parent[now]
    flow[last][now] += 1; flow[now][last] -= 1
    now = last
if sum(flow[0])==sum(column)==sum(row):
  for i in range(1,N+1):
    for j in range(N+1,N+M+1):
      if flow[i][j] and (parent:=update(i,j)):
        flow[i][j] -= 1
        while j!=i:
          last = parent[j]
          flow[last][j] += 1; flow[j][last] -= 1
          j = last
  for i in range(1,N+1):
    print(*flow[i][N+1:-1],sep="")
else:
  print(-1)