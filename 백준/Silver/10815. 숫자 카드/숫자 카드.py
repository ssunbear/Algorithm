import sys
input=sys.stdin.readline

n=int(input())
card=list(map(int, input().split()))
k=int(input())
expect=list(map(int, input().split()))

card.sort()
check=[0]*k

for i in range(k):
    start, end = 0, n-1
    while start<=end:
        mid=(start+end)//2
        if card[mid] == expect[i]:
            check[i]=1
            break
        elif card[mid]> expect[i]:
            end=mid-1
        else:
            start=mid+1

print(*check)
    