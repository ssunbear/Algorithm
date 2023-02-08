import sys
input=sys.stdin.readline

d=[]
dchar="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

n,b= map(int,input().split())
while n>0:
    d+=dchar[n%b]
    n//=b

print("".join(d[::-1]))
