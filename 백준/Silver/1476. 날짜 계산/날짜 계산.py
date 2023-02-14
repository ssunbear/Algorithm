import sys
input=sys.stdin.readline

e, s, m= map(int, input().split())

year=s
if e==15: e=0
if s==28: s=0
if m==19: m=0

while True:
    if year%15==e and year%28==s and year%19==m:
       print(year)
       break
    else: year +=28