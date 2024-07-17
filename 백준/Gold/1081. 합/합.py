def page(num,n):
    c=len(str(num))-1
    a=int(str(num)[0])

    if c==0: 
        if n>a: return 0
        else: return 1
    
    tmp=a*c*10**(c-1) +page(num-a*10**c,n)

    if n>a: return tmp
    elif n==a: return tmp+(num-a*10**c+1)
    else: return tmp + 10**c


def sumcount(num):
    result=0
    for i in range(1,10):
        result+=i*page(num,i)
    return result

L,U=map(int,input().split())
if L>0: 
    print(sumcount(U)-sumcount(L-1))
else:
    print(sumcount(U)-sumcount(L))