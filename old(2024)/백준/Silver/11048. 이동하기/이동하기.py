## 패딩 준 버젼. 인덱스 덜 헷갈리긴 하는 듯.

n, m = map(int, input().split())
arr = [[0]*(m+1)] + [[0]+list(map(int, input().split())) for _ in range(n)]


# d[i][j] = d[i-1][j] + d[i][j-1]
# 디피 테이블 (좌, 상 패딩 + 1)
d = [[0] * (m + 1) for _ in range(n+1)]
# 초기값 생략

for i in range(1, n+1):
    for j in range(1, m+1):
        d[i][j] = max(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + arr[i][j]

print(d[n][m])
