n = int(input())
dict = {0:0, 1:1, 2:1}
m=1000000007
def fibo(n):
    if n==0 or n==1 or n==2: 
        return dict[n]
    
    a = n // 3
    if not n in dict.keys():
        if n >= 100:
            dict[n] = (fibo(a) * fibo(n-a+1) + fibo(a-1) * fibo(n-a)) % m
        else:
            dict[n] = (fibo(n-1) + fibo(n-2)) % m
        
    return dict[n]

if n % 2 == 1: print(fibo(n+1))
else: print(fibo(n))