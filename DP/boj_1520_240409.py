import sys
from heapq import heappush, heappop

input = sys.stdin.readline


# BFS 함수 정의
def bfs(r, c):
    # 시작점
    dp[0][0] = 1
    heap = []  # 최대힙
    heappush(heap, (arr[r][c] * -1, r, c))

    # 방문예약 탐색
    while heap:
        # 꺼내기
        height, cr, cc = heappop(heap)

        # 다음 방문
        for nr, nc in [(cr - 1, cc), (cr + 1, cc), (cr, cc - 1), (cr, cc + 1)]:
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == -1 : # 범위 내고 방문 x
                if arr[nr][nc] >= arr[cr][cc]: # 높이가 높다면
                    visited[nr][nc] = -1
                    continue
                if


################
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]
bfs(0, 0)
