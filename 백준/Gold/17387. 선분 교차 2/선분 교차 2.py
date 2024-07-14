def ccw(x1,y1,x2,y2,x3,y3):
# y-y1=(y2-y1)/(x2-x1) *(x-x1) -> (y-y1)(x2-x1) = (y2-y1)*(x2-x1) -> x=x3넣고 y와 y3랑 큰지 비교
    if (x2 - x1) * (y3 - y1) < (y2 - y1) * (x3 - x1): return -1
    elif (x2 - x1) * (y3 - y1) > (y2 - y1) * (x3 -x1): return 1
    else: return 0

x1,y1,x2,y2=map(int, input().split())
x3,y3,x4,y4=map(int, input().split())

# 시계 반시계, 
if ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)==0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)==0: 
    # 두 직선이 겹치면 교차
    if min(x1,x2)<=max(x3,x4) and min(x3,x4)<=max(x1,x2) and min(y1,y2)<=max(y3,y4) and min(y3,y4)<=max(y1,y2):
        print(1)
    else:
        print(0)
elif ccw(x1,y1,x2,y2,x3,y3)*ccw(x1,y1,x2,y2,x4,y4)<=0 and ccw(x3,y3,x4,y4,x1,y1)*ccw(x3,y3,x4,y4,x2,y2)<=0:
    print(1)
else: 
    print(0)