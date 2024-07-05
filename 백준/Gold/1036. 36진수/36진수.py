import sys
input = sys.stdin.readline
from collections import deque
n36 = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caldiff(num):
  L = len(num)
  for i in range(L):
    n = int(num[L-i-1],36)
    diff[n] += (35-n)*(36**i)

def make36(x):
  if x == 0:
    return 0
  dq = deque()
  while x:
    dq.appendleft(n36[x%36])
    x //= 36
  return "".join(dq)

N = int(input())

SUM = 0
diff = [0]*36

for i in range(N):
  num = input().strip()
  SUM += int(num,36)
  caldiff(num)
diff.sort(reverse=True)

K = int(input())
for i in range(K):
  SUM += diff[i]

print(make36(SUM))