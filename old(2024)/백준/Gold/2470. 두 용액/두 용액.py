####### 1. 투 포인터 사용 버전 ########

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
# 용액들 오름차순 정렬 되어 있음


start = 0
end = n - 1

cnt = 0
ans = abs(lst[start] + lst[end])
ans_start = start
ans_end = end

# 투 포인터 돌리기
while start < end:
    total = lst[start] + lst[end]
    # 갱신
    if abs(total) < ans:
        ans_start = start
        ans_end = end
        ans = abs(total)


    ## 토탈이 음수냐 양수냐가 중요했던 문제
    if total < 0:
        start += 1

    elif total == 0:
        break

    else:
        end -= 1

print(lst[ans_start], lst[ans_end])