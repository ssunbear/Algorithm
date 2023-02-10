import sys
k,n=map(int,sys.stdin.readline().split())
data=[]
for i in range(k):
    data.append(int(sys.stdin.readline()))

start, end= 1, max(data)

while start<=end:
    mid = (start+end)//2
    cnt=0
    for i in range(k):
        cnt += data[i]//mid
    if cnt>=n:
        start=mid+1
    else:
        end=mid-1
           
print(end)