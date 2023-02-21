import sys
input=sys.stdin.readline
from collections import deque
n=int(input())

q=deque([i+1 for i in range(n)])
cnt=0
while True:
    if len(q)==1:
        print(q.pop())
        break
    if cnt%2==0: q.popleft()
    else: q.append(q.popleft())
    cnt+=1