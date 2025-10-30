
n = int(input())

# 디피 테이블 끝에 패딩
d = [[0] * (11) for _ in range(n+1)]


# 값이 m인 개수 = 이전 행의 m-1 의 개수 + m+1의 개수
d[1][1:10] = [1] * 9

for i in range(2, n+1):
    for j in range(10):
        d[i][j] = d[i-1][j-1] + d[i-1][j+1]

ans = sum(d[n])
print(ans%10**9)
