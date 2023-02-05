import sys
input=sys.stdin.readline

n=int(input())
card=[]
for i in range(n):
    data=list(map(int, input().split()))
    card.append(data)

card.sort()
for i in range(n):
    print(card[i][0], card[i][1])