answer,flag=[],0
x,b=map(int,input().split())
if not (b<0 or (x>=0 and b>0)): 
    x*=(-1)
    flag=1

while x:
    Q,R=divmod(x,b)
    if R<0:
        Q+=1
        R-=b
    answer.append(R)
    x=Q

answer=''.join(map(str,answer[::-1]))

if answer:
    if flag==0:
      print(answer)  
    else:
      print(f'-{answer}')
else:
    print(0)
