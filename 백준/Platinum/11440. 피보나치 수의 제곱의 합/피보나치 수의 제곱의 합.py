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

n=int(input())
print((Fibo(n)%max)*(Fibo(n+1)%max) %max)
