import sys
input=sys.stdin.readline

def round_r(num):
    if num - int(num)>=0.5:
        return int(num)+1
    else:
        return int(num)

n=int(input())


if n:
    data=[int(input()) for _ in range(n)]
    data.sort()

    if round_r(n*0.15):
        data=data[round_r(n*0.15):-round_r(n*0.15)]

    print(round_r(sum(data)/len(data)))


else:
    print(0)