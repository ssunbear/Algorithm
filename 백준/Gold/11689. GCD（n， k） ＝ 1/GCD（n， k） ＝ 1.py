n=int(input())
ans = n

for i in range(2, int(n**0.5)+1):
    if n % i == 0:
        while n % i == 0:   
            n //= i
        ans *= (1-1/i)


if n>1: ans *= (1-1/n)
print(int(ans))