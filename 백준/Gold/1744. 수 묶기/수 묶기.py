import sys
input=sys.stdin.readline

n=int(input())
pos=[] 
neg=[]
total=0

for i in range(n):
    data=int(input())
    if data>1: pos.append(data)
    elif data==1: total+=1
    else: neg.append(data)

pos.sort(reverse=True)
neg.sort()

if len(pos)%2==0:
    for i in range(0, len(pos), 2): total+=pos[i]*pos[i+1]
else:
    for i in range(0, len(pos)-1, 2): total+=pos[i]*pos[i+1]
    total+=pos[len(pos)-1]

if len(neg)%2==0:
    for i in range(0, len(neg), 2): total+=neg[i]*neg[i+1]
else:
    for i in range(0, len(neg)-1, 2): total+=neg[i]*neg[i+1]
    total+=neg[len(neg)-1]

print(total)