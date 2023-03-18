import sys
input=sys.stdin.readline

T=int(input())
for i in range(T):
    R, C=map(int,input().split())
    x, y=min(R,C), max(R,C)-min(R,C)
    W=(int)((x*(x+1)*(2*x+1))//3+x*(x+1)*(y-1)-x*y+x)
    C=W-x
    print(W, C)