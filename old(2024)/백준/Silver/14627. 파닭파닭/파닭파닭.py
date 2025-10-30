# 14627

# 최대한의 파 /. 같은 양의 하나의 파 / 남은 파의 양

S, C = map(int, input().split())

# 파 리스트
lst = [int(input()) for _ in range(S)]

# 자른 파의 총개수 => 파닭수보단 많으면서 적을 수록 좋음 => 파 자르는 길이는 길 수록 좋음

# 이진 탐색

start = 1
end = max(lst)

while start <= end:
    # 자른파의 총개수
    s_total = 0
    mid = (start + end) // 2

    for s in lst:
        s_total += s // mid

    if s_total >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

# 정답

res = sum(lst) - C * answer
print(res)
