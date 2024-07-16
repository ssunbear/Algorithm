arr=input()
for i in range(len(arr)):
    if i==0:
        x=arr[0]
    else:
        if x[i-1]<arr[i]: x=arr[i]+x
        else: x=x+arr[i]

print(''.join(reversed(x)))