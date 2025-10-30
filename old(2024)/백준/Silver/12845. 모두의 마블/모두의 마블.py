# 입력
n = int(input())
lvs = list(map(int, input().split()))

# 최대값
max_lv = max(lvs)

# 골드 최대값 : 최대값*(n-2) + 전체의 합
sum_lv = max_lv * (n - 2) + sum(lvs)

# 출력
print(sum_lv)
