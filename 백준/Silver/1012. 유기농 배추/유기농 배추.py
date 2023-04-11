import sys
sys.setrecursionlimit(10**7)
input=sys.stdin.readline

def dfs(x,y):
    if 0>x or y<0 or x>=m or y>=n:
        return False
    if array[x][y]==1:
        array[x][y]=0
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True    
    return False

T=int(input())
for l in range(T):
  cnt1=0
  m,n,k= map(int, input().split())
  array=[[0]*n for _ in range(m)]

  for j in range(k):
    x, y= map(int,input().split())
    array[x][y]=1
  
  for i in range(m):
    for j in range(n):
      if dfs(i,j)==True:
        cnt1+=1

  print(cnt1)