def solution(park, routes):
    answer=[]
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j]=='S':
                sx,sy=i,j
                break
               
    op=[[-1,0],[0,1],[0,-1],[1,0]] #NEWS

    for route in routes:
        news,n=route.split(' ')
        n=int(n)
        nx,ny=sx,sy
        
        if news=='N': idx=0
        elif news=='E': idx=1
        elif news=='W':idx=2
        else: idx=3
        
        print(nx,ny)
        for i in range(n):
            dx,dy=op[idx][0],op[idx][1]
            if 0<=sx+dx<len(park) and 0<=sy+dy<len(park[0]) and park[sx+dx][sy+dy]!='X':
                sx,sy=sx+dx,sy+dy
            else:
                sx,sy=nx,ny
                break
                
    answer.append([sx,sy])  

    return answer[0]