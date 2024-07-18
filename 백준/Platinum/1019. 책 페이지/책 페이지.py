def page(num,n):
    c=len(str(num))-1
    a=int(str(num)[0])

    if c==0: 
        if n>a: return 0
        else: return 1
    
    tmp=a*c*10**(c-1) +page(num-a*10**c,n)

    if n>a: return tmp
    elif n==a: return tmp+(num-a*10**c+1)
    elif n==0: return tmp +(c-len(str(num-a*10**c)))*(num-a*10**c+1) +10**c
    else: return tmp + 10**c


def zero(num):
    result=0
    tmp=len(str(num))
    for i in range(tmp):
        result+=10**i
    return result

N=int(input())
print(page(N,0)-zero(N),end=' ')
for i in range(1,10):
    print(page(N,i),end=" ")