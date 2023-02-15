import sys
input=sys.stdin.readline

n=int(input())
data=[list(map(int, input().strip())) for _ in range(n)]

length=len(data[0])
for i in range(length-1, -1, -1):
    tmp=[[] for _ in range(n)]
    setA=set()
    for j in range(n):
        tmp[j].append(data[j][i:length])
        setA.add(str(tmp[j]))
    if len(setA)==n:
        print(length-i)
        break