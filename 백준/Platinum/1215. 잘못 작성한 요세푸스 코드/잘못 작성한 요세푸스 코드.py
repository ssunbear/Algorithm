n, k = map(int, input().split())

ans = 0
if n>k:
    ans += k*(n-k)

m = int(k**0.5)+1
for i in range(1, m):
    l = min(k//i, n)
    r = k//(i+1) + 1
    if l<r : continue
    ans += k*(l-r+1) - (l+r)*(l-r+1)*i//2

for i in range(1, min(k//m, n)+1):
    ans += k%i

print(ans)