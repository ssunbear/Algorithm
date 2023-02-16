import sys
input=sys.stdin.readline
from itertools import product

a, b= map(int, input().split())
cnt=1
flag=0
def check(a, b, cnt):
    global flag
    if a>b: return 0
    elif a==b:
        flag=1
        print(cnt)
    else:
        check(2*a, b, cnt+1)
        check(int(str(a)+'1'), b, cnt+1)

check(a,b,1)
if flag==0: print(-1)