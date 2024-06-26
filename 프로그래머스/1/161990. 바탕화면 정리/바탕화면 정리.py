def solution(wallpaper):
    n=len(wallpaper)
    m=len(wallpaper[0])
    #print(n,m)
    check1=[]
    check2=[]
    for i in range(n):
        for j in range(m):
            if wallpaper[i][j]=='#':
                check1.append(i)
                check1.append(i+1)
                check2.append(j)
                check2.append(j+1)
                
    #print(check1)
    #print(check2)
    answer = []
    answer.append(min(check1))
    answer.append(min(check2))
    answer.append(max(check1))
    answer.append(max(check2))
    return answer