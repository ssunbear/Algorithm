import sys
input=sys.stdin.readline

n=int(input())
card=[]
for i in range(n):
    card.append(int(input()))
card.sort()
for i in card:
    print(i)
