from collections import deque

# 델타 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def bfs(x, y):
    # 시작점 방문 처리
    arr[x][y] = 0
    q = deque()
    q.append((x, y))
    cnt = 1

    # 방문 예약 처리
    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            # 방문가능하냐
            if 0 <= nr < n and 0 <= nc < n and arr[nr][nc] == 1:
                arr[nr][nc] = 0
                q.append((nr, nc))
                cnt += 1

    return cnt


n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
totals = []

# 숫자 1 나올때마다 카운트 세면서,
group_cnt = 0  # 단지 수
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            group_cnt += 1

            # 거기서 bfs나 dfs 돌려서 연결된 애들 전부 0으로 바꿔버리기
            # 이때 단지수를 셈
            # 단지수를 totals 리스트에 넣으면 될듯.
            totals.append(bfs(i, j))

# 출력
print(group_cnt)
totals.sort()
for i in totals:
    print(i)
