import sys

n=int(input())
time =[]
for i in range(n):
    start, finish = map(int, sys.stdin.readline().split())
    time.append([start,finish])

cnt=1
time.sort(key=lambda x:x[0])
time.sort(key=lambda x:x[1])

end=time[0][1]

for i in range(1,n):
    if time[i][0]>=end:
        cnt+=1
        end=time[i][1]

print(cnt)