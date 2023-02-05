import sys
input=sys.stdin.readline

amho=[0]+list(input().strip())
if amho[1]=='0':
    print(0) 
    exit()

dp=[1,1]+[0] * (len(amho)-2)

for i in range(2, len(amho)):
    num1=int(amho[i])
    num2=int(amho[i-1])*10+int(amho[i])
    if num1>0: dp[i]+=dp[i-1]
    if num2>=10 and num2<=26: dp[i]+=dp[i-2]

print(dp[len(amho)-1]%1000000)