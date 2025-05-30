def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def convert_to_base(n, k):
    if n == 0:
        return "0"
    digits = []
    while n:
        digits.append(int(n % k))
        n //= k
    return ''.join(map(str, digits[::-1]))

def count_primes_in_base(n, k):
    # Step 1: Convert n to base k
    base_k = convert_to_base(n, k)
    
    # Step 2: Split the base_k number by '0'
    parts = base_k.split('0')
    
    # Step 3: Find primes according to the conditions
    prime_count = 0
    
    # Check each part and its neighbors
    for i in range(len(parts)):
        if parts[i] == '':
            continue
            
        # Check if the current part is prime
        num = int(parts[i])
        if is_prime(num):
            prime_count += 1
        
        # Check for the case of 0P0 (i-1 and i+1 must exist)
        if i > 0 and i < len(parts) - 1 and parts[i-1] == '' and parts[i+1] == '':
            if is_prime(num):
                prime_count += 1
        
        # Check for the case of P0 (i-1 must be empty)
        if i > 0 and parts[i-1] == '':
            if is_prime(num):
                prime_count += 1
        
        # Check for the case of 0P (i+1 must be empty)
        if i < len(parts) - 1 and parts[i+1] == '':
            if is_prime(num):
                prime_count += 1

    return prime_count

def solution(n, k):
    return count_primes_in_base(n, k)

# 예시 입력
print(solution(437674, 3))  # 출력: 3
