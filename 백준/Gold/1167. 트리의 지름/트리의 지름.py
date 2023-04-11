import sys
sys.setrecursionlimit(10**9) 
n = int(sys.stdin.readline())

def dfs(x,y):
    for a, b in tree[x]:
        if visited[a]==-1:
            visited[a]=b+y
            dfs(a,b+y)

tree=[[] for _ in range(n+1)]
for i in range(n):
    data=list(map(int, sys.stdin.readline().split()))
    for j in range(1,len(data)-2,2):
        tree[data[0]].append([data[j], data[j+1]])
        

visited =[-1]*(n+1)
visited[1]=0
dfs(1,0)

s=visited.index(max(visited))
visited =[-1]*(n+1)
visited[s]=0
dfs(s,0)

print(max(visited))