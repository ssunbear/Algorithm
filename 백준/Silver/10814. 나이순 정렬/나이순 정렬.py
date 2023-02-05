import sys
n= int(input())
data=[]
for i in range(n):
    age, name = (list(sys.stdin.readline().split()))
    data.append([age, name])

data.sort(key=lambda x : int(x[0]))

for i in range(n):
    print(data[i][0], data[i][1])
 
