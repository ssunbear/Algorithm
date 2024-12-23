import sys
input=sys.stdin.readline
n=int(input())
setA=set()
for i in range(n):
    data=input().split()
    if data[0]=="add":
        if data[1] not in setA: setA.add(data[1])
    elif data[0]=="remove":
        setA.discard(data[1])
    elif data[0]=="check":
        if data[1] in setA: print(1)
        else: print(0)
    elif data[0]=="toggle":
        if data[1] in setA: setA.discard(data[1])
        else: setA.add(data[1])
    elif data[0]=="all":
        setA.update(['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'])
    elif data[0]=="empty":
        setA.clear()
        