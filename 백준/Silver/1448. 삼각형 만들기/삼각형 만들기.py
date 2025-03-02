import sys
input=sys.stdin.readline
N = int(input().strip())            
x=[]
for i in range(N):
    x.append(int(input().strip()))

x.sort(reverse=True)
answer=-1
for i in range(N-2):
    if x[i] < x[i+1] + x[i+2]:
        answer=sum(x[i:i+3])
        break

print(answer)