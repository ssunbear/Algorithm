import sys
input=sys.stdin.readline

channel=int(input())
n=int(input())
broken=list(map(int, input().split()))

count=abs(100-channel)

for i in range(1000001):
    i=str(i)
    for j in range(len(i)):
        if int(i[j]) in broken: break
        elif j==len(i)-1:
            count=min(count, abs(int(i)-channel)+len(i))

print(count)