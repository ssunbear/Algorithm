min, max = map(int, input().split())

answer = max - min + 1
divPossible = [False] * (max-min+1)

for i in range(2, int(max**0.5+1)):
    square = i*i
    for j in range((((min-1)//square)+1)*square, max+1, square):
        if not divPossible[j-min] :
            divPossible[j-min] = True
            answer -= 1
print(answer)