import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().split()))
avg=sum(a)//n
cnt1, cnt2=0,0

for i in a:
    if i<avg: cnt1+=(avg-i)
    elif i>avg+1: cnt2+=(i-avg-1)

print(max(cnt1,cnt2))