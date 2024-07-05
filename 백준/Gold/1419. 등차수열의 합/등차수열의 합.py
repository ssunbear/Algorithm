l=int(input())
r=int(input())
k=int(input())

if k == 2:
    print(max(0, r - max(l, 3) + 1))
elif k == 3:
    print(max(0, r // 3 - (max(l, 6) - 1) // 3))
elif k == 4:
    print(max(0, r // 2 - (max(l, 14) - 1) // 2) + (l <= 10 <= r))
else:
    print(max(0, r // 5 - (max(l, 15) - 1) // 5))