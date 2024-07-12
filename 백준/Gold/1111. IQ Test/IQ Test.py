n=int(input())
arr=list(map(int, input().split()))

if n==1: print('A')
elif n==2:
    if arr[0]==arr[1]: print(arr[0])
    else: print('A')
else:
    # y = ax + b , 기울기랑 상수값 찾자
    if arr[1]-arr[0]!=0:
        a=(arr[2]-arr[1]) // (arr[1]-arr[0])
    else: 
        a=0

    b=arr[1]-a*arr[0]
    flag=0
    for j in range(n-1):
        tmp=a*arr[j]+b
        if arr[j+1]==tmp:
            continue
        else:
            print('B')
            flag=1
            break
    
    if flag!=1:
        print(arr[n-1]*a+b)
