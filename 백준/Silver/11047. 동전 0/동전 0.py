import sys
input=sys.stdin.readline

n, m= map(int, input().split())
data=[]
for i in range(n):
    data.append(int(input()))

cnt=0
data.sort(reverse=True)
for i in data:
    if m//i>=0:
        cnt+=m//i
        m-=i*(m//i)

print(cnt)