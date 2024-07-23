def count(num):  
    cnt = 0    
    binnum=bin(num)[2:]
    for i in range(len(binnum)):  
        if binnum[i] == '1':  
            val = len(binnum) -i-1  
            cnt += (one[val] + (num - 2**val + 1))
            num = num - 2 ** val  
    return cnt  

x, y = map(int, input().split())  
one = [0]*60  
for i in range(1, 60):  one[i] = 2**(i-1) + 2 * one[i-1]  
print(count(y) - count(x-1))