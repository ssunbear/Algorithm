import sys
input=sys.stdin.readline

def showActivateStr(target, isActivate):
    result = ""
    for i in range(len(isActivate)):
        if isActivate[i]:
            result += target[i]
    return result

target = input().strip()
isActivate = [False] * len(target)
for i in range(len(target)):
    # isActivate값이 False인것 하나하나에 대해서 추가했을 때의 가능한 문자열들을 모아놓고 가장 앞서는 경우를 확인
    tempResult = [] # (문자열, 그때 활성화 시킨 인덱스)
    
    for j in range(len(isActivate)):
        if isActivate[j] == False:
            isActivate[j] = True
            tempResult.append((showActivateStr(target, isActivate), j))
            isActivate[j] = False
    
    tempResult.sort() # tempResult의 가장 앞에는 (가장 앞서는 문자열, 그때 활성화 시킨 인덱스)가 될 것임
    print(tempResult[0][0])
    isActivate[tempResult[0][1]] = True