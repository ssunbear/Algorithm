import sys
input=sys.stdin.readline
from collections import deque
n,k =map(int, input().split())
queue=deque()
for i in range(1,n+1): queue.append(i)
res=[]

while queue:
    for _ in range(k-1):
        queue.append(queue.popleft())
    res.append(queue.popleft())

print(str(res). replace('[', '<'). replace(']', '>'))