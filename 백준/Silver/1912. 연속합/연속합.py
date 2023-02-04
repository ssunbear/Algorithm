import sys
input=sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))
for i in range(1,n):
    array[i]=max(array[i], array[i-1]+array[i])

print(max(array))
