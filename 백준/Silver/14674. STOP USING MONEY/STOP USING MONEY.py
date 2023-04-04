import sys
input=sys.stdin.readline

n, k=map(int, input().split())
data=[]
mod=1
for i in range(n):
    data.append(list(map(int, input().split())))
    mod*=data[i][1]

for i in range(n):
    data[i].append(data[i][2]*mod//data[i][1])

res=sorted(data, key=lambda x: (-x[3], x[1], x[0]))
for i in range(k):
    print(res[i][0])