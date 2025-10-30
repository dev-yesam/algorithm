# 우측과 하측만 갈 수 있다는 건, for 문으로 하나씩 살펴도 누락되지 않는다는 것.

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1 # 경로 개수 초기 값

for i in range(n):
    for j in range(n):
        jump = arr[i][j]
        # 경로가 있고, 점프 숫자가 있다면
        if dp[i][j] and arr[i][j] :
            # 다음 점프 디피테이블에 기록하자!
            for ni, nj in [(i+jump, j), (i, j+jump)]:
                if 0<= ni< n and 0<= nj < n :
                    dp[ni][nj] += dp[i][j]
print(dp[n-1][n-1])