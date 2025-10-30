from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    # 시작점 방문
    q = deque()
    res = 0  # 남은 0 개수
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if arr[i][j][k] == 1:
                    q.append((i, j, k))
                    # arr[i][j][k] = 1 # 이미 돼있음
                elif arr[i][j][k] == 0:
                    res += 1

    # 방문 예약 탐색
    while q:
        now_h, now_n, now_m = q.popleft()

        for d in ((1, 0, 0), (-1, 0, 0), (0, 0, -1), (0, 0, 1), (0, -1, 0), (0, 1, 0)):
            new_h, new_n, new_m = now_h + d[0], now_n + d[1], now_m + d[2]
            if 0 <= new_h < h and 0 <= new_n < n and 0 <= new_m < m and arr[new_h][new_n][new_m] == 0:
                # [1] 사전 방문 표시
                arr[new_h][new_n][new_m] = arr[now_h][now_n][now_m] + 1
                # [2] 방문 예약
                q.append((new_h, new_n, new_m))
                # [3] 방문 행동
                res -= 1

    # 다 바꿨다면?
    if res ==0:
        return arr[now_h][now_n][now_m] - 1
    else:
        return -1

# 입력
m, n, h = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

ans = bfs()
print(ans)