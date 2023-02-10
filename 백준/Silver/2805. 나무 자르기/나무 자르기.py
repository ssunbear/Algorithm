import sys
n,m=map(int,sys.stdin.readline().split())
trees=list(map(int,sys.stdin.readline().split()))
start, end= 1, max(trees)
#이진탐색 
while start <= end:
    mid=(start+end)//2
    total=0

    for tree in trees:
        if tree>mid:
            total+=tree-mid
        if total>m: break

    if total>=m:
        start=mid+1
    else:
        end=mid-1

print(end)