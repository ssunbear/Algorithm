import sys
res=0
dchar="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

data=sys.stdin.readline().split()
n=data[0]
n=n[::-1]
b=int(data[1])

for i in range(len(n)):
    res+=dchar.index(n[i])*(b**i)

print(res)