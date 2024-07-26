arr = input()
n = len(arr)
dp = [2500] * (n) + [0]
palindrome = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(i + 1):
        if arr[j] == arr[i] :
            if i - j < 2 or palindrome[j + 1][i - 1]: 
                palindrome[j][i] = 1
                dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[n - 1])