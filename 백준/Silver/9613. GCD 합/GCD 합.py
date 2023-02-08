import sys
input=sys.stdin.readline
import math

n=int(input())
for _ in range(n):
    total=0
    data=list(map(int, input().split()))
    length=data[0]
    for j in range(1, length):
        for k in range(j+1,length+1):
            total+=math.gcd(data[j], data[k])
    print(total)