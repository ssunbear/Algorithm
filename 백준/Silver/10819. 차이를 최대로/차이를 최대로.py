import sys
input=sys.stdin.readline
from itertools import permutations

n=int(input())
data=list(map(int, input().split()))
total=0

def totalsum(arr):
    global total
    tot=0
    for i in range(len(arr)-1):
        tot+=abs(arr[i]-arr[i+1])
    total=max(total,tot)
        
for i in permutations(data, n):
    totalsum(i)

print(total)