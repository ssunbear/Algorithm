prime_num_list = []

check = [0 for _ in range(4000001)]
check[0:2] = [1, 1]
for i in range(2, int(4000000**0.5)+1):
    if check[i] == 0:
        for j in range(i*2, 4000001, i):
            check[j] = 1
            
prime_num_list = [idx for idx, val in enumerate(check) if val == 0]
        
N = int(input())

left = 0
right = 0
sumNum = prime_num_list[0]

cnt = 0

while left <= right :
    if sumNum == N:
        cnt += 1
        sumNum -= prime_num_list[left]
        left += 1
    elif sumNum < N:
        if right + 1 < len(prime_num_list):
            right += 1
            sumNum += prime_num_list[right]
        else:
            # right가 끝에 도달했을 때 left만 증가
            sumNum -= prime_num_list[left]
            left += 1
    else:
        sumNum -= prime_num_list[left]
        left += 1 
    
print(cnt)