P = 1000000007

factorial=[1]*(4000001)
for i in range(2, 4000001):
    factorial[i] = (factorial[i-1] * i) % P


def pow(n, k, mod):
    if k == 1:
        return n % mod
    
    tmp=pow(n,k//2,mod)
    if k % 2:
        return (tmp * tmp * n) % mod
    else:
        return (tmp * tmp) % mod
    
for i in range(int(input())):
    n, k = map(int,input().split())
    print(factorial[n] * pow((factorial[k] * factorial[n-k]), P-2, P) % P)