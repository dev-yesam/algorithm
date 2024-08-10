n, m = map(int, input().split())
lst = [input() for _ in range(n)]

count = 0


def dfs(x, y, visited, tile):
    # 방문처리
    visited[x][y] = 1

    # 재귀호출
    if tile == "-":
        nx, ny = x, y + 1
        if ny < m and tile == lst[nx][ny]:
            dfs(nx, ny, visited, tile)
    else:
        nx, ny  = x + 1, y
        if nx < n and tile == lst[nx][ny]:
            dfs(nx, ny, visited, tile)


# 2종류의 dfs로 하면 되지 않을까? => 1종류도 충분
visited = [[0] * (m + 1) for _ in range(n)]

# 방문 ㄱㄱ
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            count += 1
            dfs(i, j, visited, lst[i][j])

# 출력
print(count)
