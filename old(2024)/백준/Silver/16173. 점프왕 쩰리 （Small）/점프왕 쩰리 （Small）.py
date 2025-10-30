import sys

sys.setrecursionlimit(10 ** 5)
n = int(input())

map = [list(map(int, input().split())) for _ in range(n)]

# 완전 탐색 하면 되는 거같은데.
visited = [[0] * n for _ in range(n)]

answer = False


def dfs(map, r, c):
    # 현재 위치 바꿀 필요 없음.
    # visited[r][c]= 1

    # 현재 방문처리
    visited[r][c] = 1

    # 이동량
    m = map[r][c]

    # 다음 위치 방문
    if r + m < n and visited[r + m][c] == 0:
        dfs(map, r + m, c)
    if c + m < n and visited[r][c + m] == 0:
        dfs(map, r, c + m)


dfs(map, 0, 0)
if visited[-1][-1] == 1:
    print('HaruHaru')
else:
    print('Hing')
