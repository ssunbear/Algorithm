import sys
input=sys.stdin.readline

n, m, k= map(int, input().split())
team=0
total=n+m
while True:
    if n>=2 and m>=1 and total>=k+3:
        n, m, total= n-2, m-1, total-3
        team+=1
    else:
        print(team)
        break