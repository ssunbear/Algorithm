import sys
input = sys.stdin.readline
m=1000000

arr = {1:1,2:1}

def Fibo(n):
  if arr.get(n):
    return arr[n]
  else:
    if n%2 == 1:
      arr[n] = (Fibo(n//2)*Fibo(n//2)+Fibo(n//2+1)*Fibo(n//2+1))%m
    else:
      arr[n] = (Fibo(n+1)-Fibo(n-1))%m
    return arr[n]

n=int(input())
print((Fibo(n))%m)