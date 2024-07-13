import sys
input = sys.stdin.readline
m=1000000000

arr = {1:1,2:1}

def Fibo(n):
  if arr.get(n):
    return arr[n]
  else:
    if n%2 == 1:
      arr[n] = (Fibo(n//2)**2+Fibo(n//2+1)**2)%m
    else:
      arr[n] = (Fibo(n+1)-Fibo(n-1))%m
    return arr[n]

a,b = map(int,input().split())
print((Fibo(b+2)-Fibo(a+1))%m)