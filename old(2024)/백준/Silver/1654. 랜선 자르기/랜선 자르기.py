# 랜선의 개수 = > 각각 랜선 // length 을 다 더하면 됨.

# 입력
k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

# 이진 탐색
start = 1
end = max(lst)
# 랜선의 길이
length = 0

while start <= end:
    mid = (start + end) // 2

    # 랜선 개수
    cnt = 0
    for i in lst:
        cnt += (i // mid)

    if cnt >= n:
        start = mid + 1
        length = mid
    else:
        end = mid - 1

print(length)
