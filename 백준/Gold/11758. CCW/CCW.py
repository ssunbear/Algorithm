p = [list(map(int, input().split())) for _ in range(3)]
# y-y1=(y2-y1)/(x2-x1) *(x-x1) -> (y-y1)(x2-x1) = (y2-y1)*(x2-x1) -> x=x3넣고 y와 y3랑 큰지 비교
if (p[1][0] - p[0][0]) * (p[2][1] - p[0][1]) < (p[1][1] - p[0][1]) * (p[2][0] - p[0][0]):
    print(-1)
elif (p[1][0] - p[0][0]) * (p[2][1] - p[0][1]) > (p[1][1] - p[0][1]) * (p[2][0] - p[0][0]):
    print(1)
else:
    print(0)
