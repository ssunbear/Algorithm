n,s=map(int,input().split())
arr=list(map(int,input().split()))

l,r=0,0
length=9999999999
total=0

while True:
    if total>=s:
        length=min(length,r-l)
        total-=arr[l]
        l+=1
    elif r==n:
        break
    else:
        total+=arr[r]
        r+=1

print(length if length !=9999999999 else 0)
