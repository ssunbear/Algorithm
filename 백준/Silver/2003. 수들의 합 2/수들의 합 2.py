import sys
input=sys.stdin.readline

N,M=map(int, input().split())
A=list(map(int, input().split()))
s,e,cnt=0,1,0

while True:
    if s>e or e>N: break

    total=sum(A[s:e])
    if total<M: e+=1
    elif total>M: s+=1
    else:
        cnt+=1
        e+=1

print(cnt)