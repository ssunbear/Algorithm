import sys
input=sys.stdin.readline

while True:
    try:
        s, t=map(str, input().split())
        idx=0
        tmp=""
        for i in range(len(t)):
            if t[i]==s[idx]:
                tmp+=s[idx]
                idx+=1
                if tmp==s:
                    print("Yes")
                    break
        else:
            print("No")
    except:
        break