MOD=1000

def mul(a,b):
    X = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                X[i][j] += a[i][k]*b[k][j] % MOD
    return X

def div(x,n): 
    if n == 1: return x
    D=div(x,n//2)
    if n % 2 == 0:
        return mul(D,D) 
    else:
        return mul(mul(D,D),x)

t = int(input())
for i in range(1,t+1):
    n = int(input())
    An = [[6,-4],[1,0]] 
    res = div(An,n)
    tmp=(res[0][0] + res[1][1] -1)%MOD
    print("Case #%d: %03d" %(i,tmp))