import sys
input=sys.stdin.readline

n, new,p=map(int,input().split())
if n==0:
    print(1)
else:
    rank=list(map(int, input().split()))
    if n==p and rank[n-1]>=new:
        print(-1)
    else:
        for i in range(n):
            if new>=rank[i]:
                print(i+1)
                break
        else:
            print(n+1)
