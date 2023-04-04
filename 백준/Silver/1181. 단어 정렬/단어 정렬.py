import sys
input=sys.stdin.readline

n=int(input())
word=[input().strip() for _ in range(n)]
A=set(word)
dic={}
for w in A:
    dic[w]=len(w)

dic1=sorted(dic.items(),  key=lambda x: (x[1],x[0]))
for i in dic1:
    print(i[0])