import sys
input=sys.stdin.readline

stack=[]
res=0
x=input().strip()
for i in range(len(x)):
    if x[i] =='(':
        stack.append(x[i])
    else:
        if x[i-1]=='(':
            stack.pop()
            res+=len(stack)
        else:
            stack.pop()
            res+=1

print(res)
