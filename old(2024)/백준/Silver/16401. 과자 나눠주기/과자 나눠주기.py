# 과자 길수록, & 과자수는 조카보다는 크거나 같

kids_num, snack_num = map(int, input().split())
snacks = list(map(int, input().split()))

# 이진 탐색

start = 1
end = max(snacks)

answer = 0
while start <= end:
    mid = (start + end) // 2

    # 과자 개수
    total = 0
    for snack in snacks:
        total += snack // mid

    if total >= kids_num:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
