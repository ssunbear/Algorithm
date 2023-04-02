import sys
input=sys.stdin.readline

n=int(input())
h=list(map(int, input().split()))
h.sort()
cnt, s, e=0,0,n-1
saveVal=0

for i in range(n):
    currentVal=h[i]-saveVal
    if currentVal<=0:
        continue
    cnt+=1
    if currentVal<h[n-1]:
        saveVal+=1

print(cnt)
