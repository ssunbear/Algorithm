import sys
input=sys.stdin.readline

data=[]
n, c =map(int, input().split())
for i in range(n):
    data.append(int(input()))

data.sort()
start, end=1, data[-1]-data[0]
answer=0

while start<=end:
    mid=(start+end)//2
    router=data[0]
    count=1

    for i in range(1, len(data)):
        if data[i]>= router+mid:
            count+=1
            router=data[i]
    if count >=c:
        start = mid +1
        answer = mid
    else:
        end=mid-1

print(answer)