from bisect import bisect_left

n = int(input())
arr = list(map(int, input().split()))
dp,index,res= [],[],[]

for i in range(n):
  x=bisect_left(dp,arr[i])
  if x < len(dp):
    dp[x]=arr[i]
  else:
    dp.append(arr[i])
  index.append(x)

tmp=max(index)    
for i in range(len(index)-1,-1,-1):
  if index[i]==tmp:
    res.append(arr[i])
    tmp-=1

res=res[::-1]
print(len(res))
print(*res)