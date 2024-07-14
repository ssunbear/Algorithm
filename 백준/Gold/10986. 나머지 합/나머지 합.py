from itertools import accumulate

n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr=list(accumulate(arr))
d=[0]*m

for i in range(len(arr)):
    d[arr[i]%m]+=1

answer=d[0]
for i in range(m):
    answer+=(d[i]*(d[i]-1)//2)

print(answer)