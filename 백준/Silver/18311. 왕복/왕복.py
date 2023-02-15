import sys
input=sys.stdin.readline

n, k=map(int, input().split())
dist=list(map(int, input().split()))

for i in range(n):
    k -= dist[i]
    if k<0:
        print(i+1)
        exit()

for i in range(n-1,-1, -1):
    k -=dist[i] 
    if k<0:
        print(i+1)
        exit()
