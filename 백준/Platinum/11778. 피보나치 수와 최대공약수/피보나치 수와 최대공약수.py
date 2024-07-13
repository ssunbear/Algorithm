import sys, math
input = sys.stdin.readline
max=1000000007

arr = {1:1,2:1}

def Fibo(n):
  if arr.get(n):
    return arr[n]
  else:
    if n%2 == 1:
      arr[n] = (Fibo(n//2)*Fibo(n//2)+Fibo(n//2+1)*Fibo(n//2+1))%max
    else:
      arr[n] = (Fibo(n+1)-Fibo(n-1))%max
    return arr[n]

n,m=map(int, input().split())
print((Fibo(math.gcd(n,m)))%max)
#피보나치 개신기..