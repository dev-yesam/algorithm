n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# 부분 집합
min_dif = 10**9
for i in range(1, 1<<n):
    sour = 1
    bitter = 0
    for j in range(n):
        if i & (1<<j):
            sour *= lst[j][0]
            bitter += lst[j][1]
    min_dif = min(min_dif, abs(sour-bitter))

print(min_dif)