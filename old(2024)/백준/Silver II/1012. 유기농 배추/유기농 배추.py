import sys

sys.setrecursionlimit(10**5)
input = sys.stdin.readline
t = int(input())


def dfs(r, c):
    # 현재 위치 방문 처리
    graph[r][c] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # 다음 위치 방문
    for x in [0,1,2,3]:
        nr = r+dr[x]
        nc = c+dc[x]
        if 0<= nr < length and 0<= nc < width and graph[nr][nc] ==1:
            dfs(nr, nc)



for tc in range(t):

    width, length, bechus = map(int, input().split())

    graph = [[0] * width for _ in range(length)]



    for _ in range(bechus):
        a, b = map(int, input().split())
        graph[b][a] = 1


    cnt = 0

    for i in range(length):
        for j in range(width):
            if graph[i][j] == 1:
                cnt += 1
                dfs(i, j)

    print(cnt)