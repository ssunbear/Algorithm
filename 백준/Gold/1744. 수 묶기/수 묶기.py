import sys

n=int(input())
pos=[] # 양수를 저장할 리스트
neg=[] # 0과 음수를 저장할 리스트 (0을 음수취급)
total=0

for i in range(n):
    num=int(sys.stdin.readline())
    if num>1:
        pos.append(num)
    elif num==1: # 1은 양수와 음수모두 만나도 더하기만 진행
        total+=1
    else:
        neg.append(num)
        
pos.sort(reverse=True)
neg.sort()

if len(pos)%2==0:
    for i in range(0, len(pos), 2):
        total+=pos[i]*pos[i+1]
else:
    for i in range(0, len(pos)-1, 2):
        total+=pos[i]*pos[i+1]
    total+=pos[len(pos)-1]

if len(neg)%2==0:
    for i in range(0, len(neg), 2):
        total+=neg[i]*neg[i+1]
else:
    for i in range(0, len(neg)-1, 2):
        total+=neg[i]*neg[i+1]
    total+=neg[len(neg)-1]

print(total)