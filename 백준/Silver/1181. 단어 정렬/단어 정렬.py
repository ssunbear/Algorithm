import sys
input=sys.stdin.readline
n=int(input())
data=[input().strip() for _ in range(n)]
A=set(data)
B={}
for x in A:
    B[x]=len(x)
C=sorted(B.items(), key= lambda x: (x[1], x[0]))
for x in C:
    print(x[0])