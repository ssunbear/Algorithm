import sys
input=sys.stdin.readline

n=int(input())
x,y=(n-1)%14, n//14
if x==0 or x==12: print("baby")
elif x==1 or x==13: print("sukhwan")
elif x==4: print("very")
elif x==5: print("cute")
elif x==8: print("in")
elif x==9: print("bed")
elif x%4==2:
    if y==0: print("tururu")
    elif y==1: print("turururu")
    elif y==2: print("tururururu")
    else: print("tu+ru*%d" %(y+2))
elif x%4==3:
    if y==0: print("turu")
    elif y==1: print("tururu")
    elif y==2: print("turururu")
    elif y==3: print("tururururu")
    else: print("tu+ru*%d" %(y+1))