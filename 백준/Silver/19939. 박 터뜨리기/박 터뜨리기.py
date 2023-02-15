import sys
input=sys.stdin.readline

n, k=map(int, input().split())

if n<k*(k+1)/2: print(-1)
elif (n-(k*(k+1)/2))%k==0: print(k-1)
else: print(k)
