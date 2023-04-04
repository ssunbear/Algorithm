import sys
input=sys.stdin.readline

n=int(input())
data=set(map(int, input().split()))
m=int(input())
data1=list(map(int, input().split()))

for i in data1:
    if i in data: print(1)
    else: print(0)