x,y = [],[]
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    x.append(a) 
    y.append(b)
x.append(x[0]) 
y.append(y[0])

X,Y = 0,0
for i in range(n):
    X+=x[i]*y[i+1]
    Y+=y[i]*x[i+1]
    
print(round(abs((X-Y)/2),1))
#https://ko.wikihow.com/%EB%8B%A4%EA%B0%81%ED%98%95-%EB%84%93%EC%9D%B4-%EA%B5%AC%ED%95%98%EA%B8%B0#:~:text=%EC%A0%95%EB%8B%A4%EA%B0%81%ED%98%95%EC%9D%98%20%EB%84%93%EC%9D%B4%EB%A5%BC%20%EA%B5%AC,%EC%9D%98%20%EC%A4%91%EC%8B%AC%EC%9C%BC%EB%A1%9C%20%EB%AA%A8%EC%9D%B4%EB%8A%94%20%EC%84%A0%EB%B6%84