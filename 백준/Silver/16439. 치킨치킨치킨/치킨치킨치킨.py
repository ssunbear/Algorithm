import sys
input=sys.stdin.readline
from itertools import combinations

n, m=map(int, input().split())
data=[list(map(int, input().split())) for _ in range(n)]

res=0
arr=[i for i in range(m)]
for a, b, c in combinations(arr, 3):
    hap=0
    for i in range(n):
        hap+=max(data[i][a], data[i][b], data[i][c])
    res=max(res, hap) 
print(res)
        