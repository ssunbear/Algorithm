import sys
from itertools import combinations
from collections import defaultdict

n,s=map(int,sys.stdin.readline().split())
m=list(map(int, sys.stdin.readline().split()))


l=m[:n//2]
r=m[n//2:]

lsum=defaultdict(int)
rsum=defaultdict(int)
lsum[0]=1
rsum[0]=1
for i in range(1,len(l)+1):
    for com in combinations(l,i):
        lsum[sum(com)]+=1

for i in range(1,len(r)+1):
    for com in combinations(r,i):
        rsum[sum(com)]+=1

lkey=sorted(lsum.keys())
rkey=sorted(rsum.keys())

res=0
l=0
r=len(rkey)-1
while l<len(lkey) and r>=0:
    if lkey[l]+rkey[r]==s:
        res+=(lsum[lkey[l]]*rsum[rkey[r]])
        l+=1
        r-=1
    elif lkey[l]+rkey[r]>s:
        r-=1
    else:
        l+=1

if s==0:
    res-=1
print(res)