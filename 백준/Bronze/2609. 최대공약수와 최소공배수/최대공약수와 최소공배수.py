import sys
input=sys.stdin.readline
import math

n ,k= map(int, input().split())
print(math.gcd(n,k))
print(math.lcm(n,k))