import sys
# import random
T = int(sys.stdin.readline())
results = []

def recur(start, a, b, c):
    for i in range(start, N):
        # i 열까지 최소
        a[i+1] = min(b[i]+1, c[i]+1)
        if zone1[i] + zone2[i] <= W: a[i+1] = min(a[i+1], a[i]+1)
        if i > 0 and zone1[i-1] + zone1[i] <= W and zone2[i-1] + zone2[i] <= W: a[i+1] = min(a[i+1], a[i-1]+2)

        if i < N-1:
            # 1행은 i+1열, 2행은 i열까지 최소 소대 수
            b[i+1] = a[i+1] + 1
            if zone1[i+1] + zone1[i] <= W: b[i+1] = min(b[i+1], c[i] + 1)

            # 1행은 i열, 2행은 i+1열까지 최소 소대 수
            c[i+1] = a[i+1]+1
            if zone2[i+1] + zone2[i] <= W: c[i+1] = min(c[i+1], b[i] + 1)
    
    return a, b, c


for _ in range(T):
    N, W = map(int, sys.stdin.readline().split())
    # 윗줄 적의 수
    zone1 = list(map(int, sys.stdin.readline().split()))
    # 아랫줄 적의 수
    zone2 = list(map(int, sys.stdin.readline().split()))
    
    # 1행과 2행 모두 i-1열까지 채울 때 최소 소대 수
    a = [0 for _ in range(N+1)]
    # 1행은 i열까지, 2행은 i-1열까지 채울 때 최소 소대 수
    b = [0 for _ in range(N+1)]
    # 1행은 i-1열까지, 2행은 i열까지 채울 때 최소 소대 수
    c = [0 for _ in range(N+1)]
    a[0] = 0
    b[0] = 1
    c[0] = 1
    a, b, c = recur(0, a, b, c)
    res = a[N]
	
    # 윗줄의 0번 열과 끝 열이 쌍을 이룰 수 있을 때 다시 한 번 계산 후 최솟값 갱신
    # 윗줄의 0번 열이 이미 채워졌다고 생각
    if N > 1 and zone1[0] + zone1[N-1] <= W:
        a[1] = 1
        b[1] = 2 # 아랫줄의 0번열, 윗줄의 1번열을 쌍을 이룰 수 없는 채로 2개의 소대를 배치해야함.
        if zone2[0] + zone2[1] <= W: c[1] = 1 # 아랫줄의 0번 열과 1번 열이 쌍을 이룰 수 있는 경우
        else: c[1] = 2
        
        a, b, c = recur(1, a, b, c)
        res = min(res, c[N-1] + 1)
        
    # 아랫줄의 0번 열과 끝 열이 쌍을 이룰 수 있을 때 다시 한 번 계산 후 최솟값 갱신
    # 아랫줄의 0번 열이 이미 채워졌다고 생각
    if N > 1 and zone2[0] + zone2[N-1] <= W:
        a[1] = 1
        c[1] = 2 # 윗줄의 0번열, 아랫줄의 1번열을 쌍을 이룰 수 없는 채로 2개의 소대를 배치해야함.
        if zone1[0] + zone1[1] <= W: b[1] = 1 # 윗줄의 0번 열과 1번 열이 쌍을 이룰 수 있는 경우
        else: b[1] = 2
        
        a, b, c = recur(1, a, b, c)
        res = min(res, b[N-1] + 1)

    # 윗줄과 아랫줄 모두 0번 열과 끝 열이 쌍을 이룰 수 있을 때 다시 한 번 계산 후 최솟값 갱신
    # 윗줄과 아랫줄 모두 0번 열이 이미 채워졌다고 생각
    if N > 1 and zone1[0] + zone1[N-1] <= W and zone2[0] + zone2[N-1] <= W:
        a[1] = 0 # 0열이 이미 채워짐
        b[1] = 1
        c[1] = 1

        a, b, c = recur(1, a, b, c)
        res = min(res, a[N-1] + 2)
    
    results.append(res)

for result in results:
    sys.stdout.write(str(result)+'\n')