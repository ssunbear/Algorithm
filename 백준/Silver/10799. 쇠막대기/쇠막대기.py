import sys
data=sys.stdin.readline().strip()
stack=[]
result=0

for i in range(len(data)):
    if data[i]=='(':
        stack.append(data[i])
    else: 
        if data[i-1]=='(': #레이저 만나면 스택크기만큼 조각잘려짐 
            stack.pop()
            result+=len(stack)
        else: # 쇠막대기 끝 한조각 추가  
            stack.pop()
            result+=1
            
print(result)