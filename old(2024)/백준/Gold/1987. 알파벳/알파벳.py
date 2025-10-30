import sys

sys.setrecursionlimit(10 * 5)

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
# lst = [[0] * C for _ in range(R)]

# bfs 로 모든 경우 탐색해서 가장 긴 경우 찾으면 될듯.
visited = []  # 그냥 알파벳으로 처리해도 됨
path = dict()
cnt = 1
ans = 0


def backtrack(r, c, visited):
    global cnt, ans
    # [1] 종료조건 => 딱히 없음.
    if cnt > ans:
        ans = cnt
    # [2] 재귀호출
    for d in ((-1, 0), (1, 0), (0, -1), (0, 1)):  # 상하좌우
        nr = r + d[0]
        nc = c + d[1]
        if 0 <= nr < R and 0 <= nc < C and arr[nr][nc] not in visited:

            k = tuple(set(visited))
            if path.get(k) == (nr, nc):
                continue
            else:
                path[k] = (nr, nc)

            cnt += 1
            backtrack(nr, nc, visited + [arr[nr][nc]])
            cnt -= 1


visited.append(arr[0][0])
backtrack(0, 0, visited)
print(ans)
