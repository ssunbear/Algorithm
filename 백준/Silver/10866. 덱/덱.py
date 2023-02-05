import sys
input=sys.stdin.readline
from collections import deque

q=deque()
n=int(input())
for i in range(n):
    action=list(input().split())
    if action[0]=="push_front":
        q.appendleft(action[1])
    elif action[0]=="push_back":
        q.append(action[1])
    elif action[0]=="pop_front":
        if q: print(q.popleft())
        else: print(-1)
    elif action[0]=="pop_back":
        if q: print(q.pop())
        else: print(-1)
    elif action[0]=="size":
        print(len(q))
    elif action[0]=="empty":
        if q: print(0)
        else: print(1)
    elif action[0]=="front":
        if q: print(q[0])
        else: print(-1)
    elif action[0]=="back":
        if q: print(q[-1])
        else: print(-1)