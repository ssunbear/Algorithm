from itertools import combinations
t=int(input())

for i in range(t):
    n=int(input())
    points = [] 
    total_x,total_y = 0,0

    for j in range(n):
        x,y = map(int,input().split())
        total_x += x  
        total_y += y 
        points.append((x,y))

    comb = list(combinations(points, n//2))
    ans=5e5
    
    for com in comb[:len(comb)//2]: 
        x1,y1 = 0,0
        for x,y in com:
            x1 += x ; 
            y1 += y
        x2,y2 = total_x-x1,total_y-y1 
        
        total_distance = ((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))**(0.5) 
        ans=min(ans,total_distance)
    print(ans)