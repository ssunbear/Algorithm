import sys
input=sys.stdin.readline
import math

n ,k= map(int, input().split())
print('1'*math.gcd(n,k))
