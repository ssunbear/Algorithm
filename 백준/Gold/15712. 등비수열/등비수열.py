a, r, n, mod=map(int,input().split())

def f(r,n,mod):
    if n==1: 
        return 1
    
    else:
        if n%2==1:
            return (f(r,n-1,mod)+pow(r,n-1,mod))%mod    
        else:
            return (f(r,n//2,mod))*(pow(r,n//2,mod)+1)%mod    

print(a*f(r,n,mod)%mod)