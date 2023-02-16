import sys
input=sys.stdin.readline

arr=input().strip()
data=[] 
n=int(input())
for i in range(n):
    data.append(input().strip())

for i in range(26):
    tmp=""
    for j in range(len(arr)):
        tmp+=chr(((ord(arr[j])-ord('a')+i)%26)+ord('a'))

    for k in range(n):
        if data[k] in tmp:
            print(tmp)
            break
