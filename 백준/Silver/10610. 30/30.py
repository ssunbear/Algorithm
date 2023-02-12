import sys
input=sys.stdin.readline

data=list(input().strip())
data.sort(reverse=True)
total=0
for x in data: total+=int(x)
if data[-1]=='0' and total%3==0: print(''.join(data))
else: print(-1)