# 문어박사 2294 참고

n, k = map(int, input().split())  # 합이 k원이 되어야함.
arr = []
for _ in range(n):
    coin = int(input())
    if coin <= k:
        arr.append(coin)
arr = list(set(arr))

dp = [k + 1] * (k + 1)
dp[0] = 0

for coin in arr:
    for i in range(k + 1):
        if i - coin >= 0:
            dp[i] = min(dp[i], dp[i - coin] + 1)

ans = dp[k]
if dp[k] == k + 1:
    ans = -1

print(ans)
