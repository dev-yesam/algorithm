n = int(input())
lst = [0] + list(map(int, input().split()))

dp = [0] * (n + 1)
for i in range(1, n + 1):
    max_length = 0
    for j in range(1, i):
        if lst[j] < lst[i]:
            max_length = max(dp[j], max_length)
    dp[i] = max_length+1

print(max(dp))