import sys, math
input=sys.stdin.readline

visited=[False,False]+ [True]*(1005000)
for i in range(2,int(math.sqrt(1005001))+1):
    if visited[i]==True:
        for j in range(2*i,1005001, i):
            visited[j]=False

def check(n):
    tmp=str(n)
    tmp1=tmp[::-1]
    if tmp==tmp1: return 1
    else: return 0

n=int(input())

for i in range(n,1005001):
    if check(i)==1 and visited[i]==True:
        print(i)
        break