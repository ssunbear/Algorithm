import sys
input=sys.stdin.readline
from itertools import product

n,k=map(int,input().split())
for i in product(range(1,n+1), repeat=k): print(*i)