import sys
n = int(sys.stdin.readline())
dic={}
for i in range(n):
    card=int(sys.stdin.readline())
    if card in dic.keys():
        dic[card]+=1
    else:
        dic[card]=1

dic1=sorted(dic.items(),key=lambda x:(-x[1],x[0]))
print(dic1[0][0])