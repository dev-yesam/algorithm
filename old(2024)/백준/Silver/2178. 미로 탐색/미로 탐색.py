from collections import deque

n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]


def bfs():
    queue = deque()
    queue.append((0, 0))
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while True:
        ci, cj = queue.popleft()
        # 도착 한다면?
        if ci == n - 1 and cj == m - 1:
            return visited[ci][cj]

        for ni, nj in ((ci - 1, cj), (ci + 1, cj), (ci, cj - 1), (ci, cj + 1)):
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj] and arr[ni][nj] == '1':
                visited[ni][nj] = visited[ci][cj] + 1
                queue.append((ni, nj))


print(bfs())
