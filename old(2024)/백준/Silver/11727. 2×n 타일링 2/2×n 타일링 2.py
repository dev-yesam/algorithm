n = int(input())
# dp 문제

# 타일 우측 끝 경우
# 1) | 로 끝나거나 (d[i-1]* 1)
# 2) = ㅁ 으로 끝나는 밖에 없음 (d[i-2] * 2)

d = [0] * (n + 3)

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2] * 2

ans = d[n]
print(ans % 10007)
