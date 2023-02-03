n=int(input())
res=[0]*(1001)
res[1]=1
res[2]=3
for i in range(3,n+1):
    res[i]=res[i-1]+2*res[i-2]

print(res[n]%10007)