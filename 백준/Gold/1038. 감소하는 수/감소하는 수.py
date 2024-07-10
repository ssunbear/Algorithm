from itertools import combinations

n = int(input())

result = []
for i in range(1, 11):
	for k in combinations(range(10), i):
		num = ''.join(list(map(str, reversed(list(k)))))
		result.append(int(num))

result.sort()
if n<len(result):
    print(result[n])
else: print(-1)