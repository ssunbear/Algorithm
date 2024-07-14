P = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % P
    return result

def pow(n, k, mod):
    if k == 1:
        return n % mod
    
    tmp=pow(n,k//2,mod)
    if k % 2:
        return (tmp * tmp * n) % mod
    else:
        return (tmp * tmp) % mod
    

n, k = map(int,input().split())
print(factorial(n) * pow((factorial(k) * factorial(n-k)), P-2, P) % P)