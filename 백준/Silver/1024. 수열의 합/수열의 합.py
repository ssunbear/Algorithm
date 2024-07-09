import sys
input = sys.stdin.readline

n,l = map(int,input().split())

result = -1

for i in range(l,101):
    j = 0.5*(2*n/i - i+1)
    if j.is_integer():
        result = [k for k in range(int(j),int(j+i))]
        if -1 in result:
            result = -1
            continue
        break
    

if result == -1:
    print(result)
else:
    for i in result:
        print(i,end=' ')
    print()