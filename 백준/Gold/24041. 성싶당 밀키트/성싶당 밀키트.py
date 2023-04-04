import sys
from collections import defaultdict
input=sys.stdin.readline

n, g, k =map(int, input().split())
info = defaultdict(list)
for i in range(n):
    s, l, o=map(int,input().split())
    info[o].append((s,l))

def countg(x, k):
    res=0
    for s, l in info[0]:
        res+=s*max(1,x-l)
    info[1].sort(key=lambda a: -a[0]*max(1,x-a[1]))
    for i in range(k, len(info[1])):
        s,l=info[1][i] 
        res+=s*max(1,x-l)
    return res

res=0
l, r= 0, int(2e9)
while True:
    if l>r:
        break
    m=(l+r)//2
    G=countg(m,k)
    if G<=g:
        res=m
        l=m+1
    else:
        r=m-1

print(res)