# n 수열 수  m 합이 될 기준
n, m = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
start = end = 0
interval_sum = nums[0]
while True:

    # 구간 합 작다면?
    if interval_sum < m:
        end += 1
        if end < n:
            interval_sum += nums[end]
        else:
            break

    # 구간 합 같다면?
    elif interval_sum == m:
        cnt += 1
        interval_sum -= nums[start]
        start += 1

    # 구간 합 작다면?
    else:
        interval_sum -= nums[start]
        start += 1

print(cnt)